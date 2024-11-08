import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
import pymysql
from datetime import datetime

province_capitals = {
    'beijing': '北京市',
    'tianjin': '天津市',
    'shanghai': '上海市',
    'chongqing': '重庆市',
    'haerbin': '哈尔滨市',
    'changchun': '长春市',
    'shenyang': '沈阳市',
    'jinan': '济南市',
    'taiyuan': '太原市',
    'huhehaote': '呼和浩特市',
    'nanjing': '南京市',
    'hangzhou': '杭州市',
    'hefei': '合肥市',
    'fuzhou': '福州市',
    'nanchang': '南昌市',
    'zhengzhou': '郑州市',
    'wuhan': '武汉市',
    'changsha': '长沙市',
    'guangzhou': '广州市',
    'nanning': '南宁市',
    'haikou': '海口市',
    'chengdu': '成都市',
    'guiyang': '贵阳市',
    'kunming': '昆明市',
    'lasa': '拉萨市',
    'yinchuan': '银川市',
    'lanzhou': '兰州市',
    'xining': '西宁市',
    'urumqi': '乌鲁木齐市',
}

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

# 创建一个空的DataFrame来存储结果
results = pd.DataFrame(columns=['city'] + candidate_labels)

# 遍历所有省会城市
for city_name in province_capitals.values():
    # 如果城市名以“市”结尾，去掉“市”
    if city_name.endswith('市'):
        city_name_short = city_name[:-1]
    else:
        city_name_short = city_name

    # 查询数据库
    query = f"SELECT city, comment FROM youtube_comments WHERE city = '{city_name}' OR city = '{city_name_short}'"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    # 将查询结果转换为DataFrame
    df = pd.DataFrame(data, columns=['city', 'comment'])

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

# 将结果插入到数据库表 emotion_youtube
insert_time = datetime.now()
with connection.cursor() as cursor:
    for index, row in results.iterrows():
        sql = """
            INSERT INTO emotion_youtube (cityName, joyNum, sadnessNum, angerNum, fearNum, surpriseNum, loveNum, disgustNum, travelNum, foodNum, sportsNum, technologyNum, healthNum, educationNum, entertainmentNum, politicsNum, platform, insert_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'youtube', %s)
        """
        cursor.execute(sql, (
            row['city'], row['joy'], row['sadness'], row['anger'], row['fear'], row['surprise'], row['love'], row['disgust'], row['travel'], row['food'], row['sports'], row['technology'], row['health'], row['education'], row['entertainment'], row['politics'], insert_time
        ))

    # 提交事务
    connection.commit()

# 关闭数据库连接
connection.close()

print("结果已成功保存到数据库表 emotion_youtube")