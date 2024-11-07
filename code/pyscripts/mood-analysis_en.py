import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
import pymysql
import sys

# 检查是否提供了输入文件
if len(sys.argv) != 2:
    print("Usage: python mood-analysis_en.py <city_name>")
    sys.exit(1)

# 获取城市中文名
city_name = sys.argv[1]

# 数据库连接配置
db_user = 'root'
db_password = '123456'
db_host = 'localhost'
db_port = 3306  # 默认MySQL端口
db_name = 'ry-vue'

# 创建数据库连接
connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    port=db_port
)


# 检查是否有可用的GPU
device = 0 if torch.cuda.is_available() else -1

# 加载预训练的tokenizer和模型
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-mnli")
model = AutoModelForSequenceClassification.from_pretrained("facebook/bart-large-mnli")

# 创建零样本分类的pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", tokenizer="facebook/bart-large-mnli", device=device)

# 候选标签
candidate_labels = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'love', 'disgust', 'travel', 'food', 'sports', 'technology', 'health', 'education', 'entertainment', 'politics']

# 查询数据库
query = f"SELECT city, comment FROM youtube_comments WHERE city = '{city_name}'"
cursor = connection.cursor()
cursor.execute(query)
data = cursor.fetchall()
# 将查询结果转换为DataFrame
df = pd.DataFrame(data, columns=['city', 'comment'])

# 关闭数据库连接
connection.close()

# 创建一个空的DataFrame来存储结果
results = pd.DataFrame(columns=['city'] + candidate_labels)

a = 0
# 分析每个comment的情感标签
for index, row in df.iterrows():
    a += 1
    if a > 100:
        break
    city = row['city']
    comment = row['comment']
    print(f"正在分析 {city} 的评论: {comment}")
    result = classifier(comment, candidate_labels, multi_label=True)
    
    # 初始化城市的情感计数
    if city not in results['city'].values:
        results = pd.concat([results, pd.DataFrame([[city] + [0]*len(candidate_labels)], columns=['city'] + candidate_labels)], ignore_index=True)
    
    # 选择概率最高的几个标签
    top_labels = [label for label, score in zip(result['labels'], result['scores']) if score > 0.5]
    
    # 统计每个标签的结果
    for label in top_labels:
        results.loc[results['city'] == city, label] += 1

# 保存结果到csv文件
output_file = 'output.csv'
results.to_csv(output_file, index=False)

print(f"结果已保存到 {output_file}")