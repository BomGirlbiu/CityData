import pandas as pd
import pymysql
from datetime import datetime

# 读取xlsx文件
file_path = './temp/target/merged_youtube_comments.xlsx'
df = pd.read_excel(file_path)

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

try:
    with connection.cursor() as cursor:
        # 插入数据
        for index, row in df.iterrows():
            city = row['city']
            comment = row['comment']
            time_published = row['time_published']
            likes = row['likes']
            insert_time = datetime.now()

            sql = """
                INSERT INTO youtube_comments (city, comment, time_published, likes, insert_time)
                VALUES (%s, %s, %s, %s, %s)
            """
            try:
                cursor.execute(sql, (city, comment, time_published, likes, insert_time))
                connection.commit()
            except Exception as e:
                print(f"插入数据失败: {e}")
                continue

    # 提交事务
    print("数据已成功保存到数据库表 youtube_comments")

finally:
    connection.close()