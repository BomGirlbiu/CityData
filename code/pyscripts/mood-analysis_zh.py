from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import csv
import sys
import os

# 初始化模型和分词器
tokenizer = T5Tokenizer.from_pretrained("ClueAI/PromptCLUE-base-v1-5", legacy=False)
model = T5ForConditionalGeneration.from_pretrained("ClueAI/PromptCLUE-base-v1-5")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"使用设备: {device}")
model.to(device)

# 预处理和后处理函数
def preprocess(text):
    return text.replace("\n", "_")

def postprocess(text):
    return text.replace("_", "\n")

def answer(text, sample=False, top_p=0.8):
    text = preprocess(text)
    encoding = tokenizer(text=[text], truncation=True, padding=True, max_length=768, return_tensors="pt").to(device)
    if not sample:
        out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_length=128, num_beams=4,
                             length_penalty=0.6)
    else:
        out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_length=64,
                             do_sample=True, top_p=top_p)
    out_text = tokenizer.batch_decode(out["sequences"], skip_special_tokens=True)
    return postprocess(out_text[0])

# 读取CSV文件并生成答案
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("用法: python mood-analysis.py <csv文件路径> <列索引>")
        sys.exit(1)

    input_file = sys.argv[1]
    column_index = int(sys.argv[2])

    if not os.path.isfile(input_file):
        print(f"文件 {input_file} 不存在")
        sys.exit(1)

    output_file = os.path.splitext(input_file)[0] + '_with_answers.csv'

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # 可选：跳过标题行（如果CSV文件有标题行）
        headers = next(reader, None)
        if headers:
            writer.writerow(headers + ['Answer'])  # 添加新列标题

        # 遍历CSV文件中的每一行
        for row in reader:
            category_value = row[column_index]  # 使用指定的列索引
            # print(f"正在处理:{category_value}")
            input_string = "情感分析：" + category_value + "选项：喜欢，厌恶，归属感，疏离感，自豪，安全，感激，无聊 答案："
            answer_text = answer(input_string)  # 生成答案
            print(answer_text)
            row.append(answer_text)  # 将答案添加到当前行
            writer.writerow(row)  # 写入新行到输出文件

    print(f"处理完成，结果已保存到 {output_file}")