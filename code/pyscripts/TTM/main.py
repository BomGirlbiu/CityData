# Standard
import os
import sys
import math
import tempfile
import torch

# Third Party
import torch
from torch.optim import AdamW
from torch.optim.lr_scheduler import OneCycleLR
from transformers import EarlyStoppingCallback, Trainer, TrainingArguments, set_seed
import numpy as np
import pandas as pd


# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取需要添加的目录路径
custom_path = os.path.join(current_dir, 'tsfm')

# 将自定义路径添加到 sys.path
if custom_path not in sys.path:
    sys.path.append(custom_path)

# First Party
from tsfm.notebooks.hfdemo.tinytimemixer.utils import (
    count_parameters,
    get_data,
    plot_preds,
)

# Local
from tsfm.tsfm_public.models.tinytimemixer import TinyTimeMixerForPrediction
from tsfm.tsfm_public.toolkit.callbacks import TrackingCallback

# Set seed for reproducibility
SEED = 42
set_seed(SEED)

# DATA ROOT PATH
# Make sure to download the target data (here ettm2)
# on the `DATA_ROOT_PATH` folder.
# ETT is available at: https://github.com/zhouhaoyi/ETDataset/tree/main
target_dataset = "ettm2"
DATA_ROOT_PATH = "datasets/"

# Results dir
OUT_DIR = "ttm_finetuned_models/"

# TTM model branch
# Use "1024_96_v1" to use 1024-96 model
TTM_MODEL_REVISION = "main"


def zeroshot_eval(
    dataset_name,
    batch_size,
    context_length=512,
    forecast_length=96,
    prediction_filter_length=None
):
    # Get data
    _, _, dset_test = get_data(dataset_name=dataset_name,
                               context_length=context_length,
                               forecast_length=forecast_length,
                               fewshot_fraction=1.0,
                               data_root_path=DATA_ROOT_PATH
                               )

    # Load model
    if prediction_filter_length is None:
        zeroshot_model = TinyTimeMixerForPrediction.from_pretrained(
            "granite-timeseries-ttm-r2", revision=TTM_MODEL_REVISION
        )
    else:
        if prediction_filter_length <= forecast_length:
            zeroshot_model = TinyTimeMixerForPrediction.from_pretrained(
                "ibm/TTM", revision=TTM_MODEL_REVISION, prediction_filter_length=prediction_filter_length
            )
        else:
            raise ValueError(
                f"`prediction_filter_length` should be <= `forecast_length")
    temp_dir = tempfile.mkdtemp()
    # zeroshot_trainer
    zeroshot_trainer = Trainer(
        model=zeroshot_model,
        args=TrainingArguments(
            output_dir=temp_dir,
            per_device_eval_batch_size=batch_size,
        )
    )
    # evaluate = zero-shot performance
    print("+" * 20, "Test MSE zero-shot", "+" * 20)
    zeroshot_output = zeroshot_trainer.evaluate(dset_test)
    print(zeroshot_output)

    # plot
    plot_preds(trainer=zeroshot_trainer, dset=dset_test, plot_dir=os.path.join(
        OUT_DIR, dataset_name), plot_prefix="test_zeroshot", channel=0)


def fewshot_finetune_eval(
    dataset_name,
    batch_size,
    learning_rate=0.001,
    context_length=512,
    forecast_length=96,
    fewshot_percent=5,
    freeze_backbone=True,
    num_epochs=50,
    save_dir=OUT_DIR,
    prediction_filter_length=None
):

    out_dir = os.path.join(save_dir, dataset_name)

    print("-" * 20, f"Running few-shot {fewshot_percent}%", "-" * 20)

    # Data prep: Get dataset
    dset_train, dset_val, dset_test = get_data(
        dataset_name,
        context_length,
        forecast_length,
        fewshot_fraction=fewshot_percent / 100,
        data_root_path=DATA_ROOT_PATH
    )

    # change head dropout to 0.7 for ett datasets
    if "ett" in dataset_name:
        if prediction_filter_length is None:
            finetune_forecast_model = TinyTimeMixerForPrediction.from_pretrained(
                "granite-timeseries-ttm-r1", revision=TTM_MODEL_REVISION, head_dropout=0.7
            )
        elif prediction_filter_length <= forecast_length:
            finetune_forecast_model = TinyTimeMixerForPrediction.from_pretrained(
                "granite-timeseries-ttm-r1", revision=TTM_MODEL_REVISION, head_dropout=0.7, prediction_filter_length=prediction_filter_length
            )
        else:
            raise ValueError(
                f"`prediction_filter_length` should be <= `forecast_length")
    else:
        if prediction_filter_length is None:
            finetune_forecast_model = TinyTimeMixerForPrediction.from_pretrained(
                "granite-timeseries-ttm-r1", revision=TTM_MODEL_REVISION,
            )
        elif prediction_filter_length <= forecast_length:
            finetune_forecast_model = TinyTimeMixerForPrediction.from_pretrained(
                "granite-timeseries-ttm-r1", revision=TTM_MODEL_REVISION, prediction_filter_length=prediction_filter_length
            )
        else:
            raise ValueError(
                f"`prediction_filter_length` should be <= `forecast_length")
    if freeze_backbone:
        print(
            "Number of params before freezing backbone",
            count_parameters(finetune_forecast_model),
        )

        # Freeze the backbone of the model
        for param in finetune_forecast_model.backbone.parameters():
            param.requires_grad = False

        # Count params
        print(
            "Number of params after freezing the backbone",
            count_parameters(finetune_forecast_model),
        )

    print(f"Using learning rate = {learning_rate}")
    finetune_forecast_args = TrainingArguments(
        output_dir=os.path.join(out_dir, "output"),
        overwrite_output_dir=True,
        learning_rate=learning_rate,
        num_train_epochs=num_epochs,
        do_eval=True,
        evaluation_strategy="epoch",
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        dataloader_num_workers=8,
        report_to=None,
        save_strategy="epoch",
        logging_strategy="epoch",
        save_total_limit=1,
        # Make sure to specify a logging directory
        logging_dir=os.path.join(out_dir, "logs"),
        load_best_model_at_end=True,  # Load the best model when training ends
        metric_for_best_model="eval_loss",  # Metric to monitor for early stopping
        greater_is_better=False,  # For loss
    )

    # Create the early stopping callback
    early_stopping_callback = EarlyStoppingCallback(
        # Number of epochs with no improvement after which to stop
        early_stopping_patience=10,
        # Minimum improvement required to consider as improvement
        early_stopping_threshold=0.0,
    )
    tracking_callback = TrackingCallback()

    # Optimizer and scheduler
    optimizer = AdamW(finetune_forecast_model.parameters(), lr=learning_rate)
    scheduler = OneCycleLR(
        optimizer,
        learning_rate,
        epochs=num_epochs,
        steps_per_epoch=math.ceil(len(dset_train) / (batch_size)),
    )

    finetune_forecast_trainer = Trainer(
        model=finetune_forecast_model,
        args=finetune_forecast_args,
        train_dataset=dset_train,
        eval_dataset=dset_val,
        callbacks=[early_stopping_callback, tracking_callback],
        optimizers=(optimizer, scheduler),
    )

    # Fine tune
    finetune_forecast_trainer.train()

    # Evaluation
    print(
        "+" * 20, f"Test MSE after few-shot {fewshot_percent}% fine-tuning", "+" * 20)
    fewshot_output = finetune_forecast_trainer.evaluate(dset_test)
    print(fewshot_output)
    print("+" * 60)

    # plot
    plot_preds(trainer=finetune_forecast_trainer, dset=dset_test, plot_dir=os.path.join(
        OUT_DIR, dataset_name), plot_prefix="test_fewshot", channel=0)


model = TinyTimeMixerForPrediction.from_pretrained(
                "granite-timeseries-ttm-r2", revision=TTM_MODEL_REVISION
            ) 
temp_dir = tempfile.mkdtemp()
zeroshot_trainer = Trainer(
        model=model,
        args=TrainingArguments(
            output_dir=temp_dir,
            per_device_eval_batch_size=64,
        )
    )

_, _, dset_test = get_data(dataset_name=target_dataset,
                            context_length=512,
                            forecast_length=96,
                            fewshot_fraction=1.0,
                            data_root_path=DATA_ROOT_PATH
                            )
# zeroshot_output = zeroshot_trainer.evaluate(dset_test)
device = torch.cuda.current_device(
    ) if torch.cuda.is_available() else torch.device("cpu")
random_indices = np.random.choice(len(dset_test), size=10, replace=False)
random_samples = torch.stack([dset_test[i]["past_values"]
                                for i in random_indices])
output = zeroshot_trainer.model(random_samples.to(device=device))
print(output)
# print(zeroshot_output)
# zeroshot_eval(dataset_name=target_dataset, batch_size=64)

# fewshot_finetune_eval(dataset_name=target_dataset, batch_size=64)
