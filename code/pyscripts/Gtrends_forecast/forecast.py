# pip install git+https://github.com/amazon-science/chronos-forecasting.git
import sys
import os
import pandas as pd
import numpy as np
import torch
import pymysql
from chronos import ChronosPipeline

# 检查参数
if len(sys.argv) != 3:
    print("Usage: python forecast.py <google|youtube> <city_name>")
    sys.exit(1)

search_type = sys.argv[1]
city_name = sys.argv[2]

if search_type not in ["google", "youtube"]:
    print("Invalid search type. Use 'google' or 'youtube'.")
    sys.exit(1)

# 连接到MySQL数据库
conn = pymysql.connect(host='localhost', user='root', password='20020316', db='ry-vue', charset='utf8')
cursor = conn.cursor()

# 从数据库中读取数据
table_name = f"{search_type}_search"
sql = f"SELECT date, count FROM {table_name} WHERE city = %s"
cursor.execute(sql, (city_name,))
data = cursor.fetchall()

# 关闭数据库连接
cursor.close()
conn.close()

# 将数据保存到DataFrame
df = pd.DataFrame(data, columns=["date", "count"])
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
# 进行预测
pipeline = ChronosPipeline.from_pretrained(
  "amazon/chronos-t5-tiny",
  device_map='cuda' if torch.cuda.is_available() else 'cpu',
  torch_dtype=torch.bfloat16,
)
context = torch.tensor(df["count"])
prediction_length = 12
forecast = pipeline.predict(context, prediction_length)

# 生成预测日期
last_date = df.index[-1]
forecast_dates = [last_date + pd.Timedelta(days=i) for i in range(1, prediction_length + 1)]

# 保存预测结果
forecast_df = pd.DataFrame({
    "Date": forecast_dates,
    "Median Forecast": np.median(forecast[0].numpy(), axis=0),
    "Low Forecast": np.quantile(forecast[0].numpy(), 0.1, axis=0),
    "High Forecast": np.quantile(forecast[0].numpy(), 0.9, axis=0)
})
# plt.figure(figsize=(8, 4))
# plt.plot(df["city"], color="royalblue", label="historical data")
if not os.path.exists("./temp"):
    os.makedirs("./temp")
forecast_df.to_csv(f"./temp/forecast_results_{city_name}.csv", index=False)
print(f'./temp/forecast_results_{city_name}.csv saved')