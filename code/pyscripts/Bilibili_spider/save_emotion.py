import pandas as pd
import pymysql

# 读取Excel文件
file_path = './temp/target/城市情感分析结果.xlsx'
df = pd.read_excel(file_path)

# 添加platform字段
df['platform'] = 'bilibili'

# 重命名列以匹配数据库表的列名
df.columns = ['cityName', 'positiveNum', 'neutralNum', 'negativeNum', 'platform']

# 连接到MySQL数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', db='ry-vue', charset='utf8')
cursor = conn.cursor()

# 插入数据到emotion_bili表
insert_sql = """
INSERT INTO emotion_bili (cityName, positiveNum, neutralNum, negativeNum, platform, insert_time)
VALUES (%s, %s, %s, %s, %s, NOW())
"""

for index, row in df.iterrows():
    cursor.execute(insert_sql, (row['cityName'], row['positiveNum'], row['neutralNum'], row['negativeNum'], row['platform']))

# 提交事务
conn.commit()

# 关闭数据库连接
cursor.close()
conn.close()

print("数据已成功插入到emotion_bili表中")