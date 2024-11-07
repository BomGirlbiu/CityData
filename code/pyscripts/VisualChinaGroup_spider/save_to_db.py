import pandas as pd
import pymysql

# 读取Excel文件
file_path = './temp/target/combined_news_img_zh.xlsx'
df = pd.read_excel(file_path)

# 连接到MySQL数据库
conn = pymysql.connect(
    host='localhost',  # 替换为你的数据库主机
    user='root',  # 替换为你的数据库用户名
    password='123456',  # 替换为你的数据库密码
    database='ry-vue',  # 替换为你的数据库名称
    charset='utf8mb4'
)
cursor = conn.cursor()
print('inserting data to city_images table...')
# 插入数据到city_images表
for index, row in df.iterrows():
    try:
        sql = "INSERT INTO city_images (city, province, imagesURL) VALUES (%s, %s, %s)"
        cursor.execute(sql, (row['City'], row['Province'], row['Image Source URL']))
    except pymysql.MySQLError as e:
        print(f"Error inserting row {index}: {e}")

# 提交事务
conn.commit()
print('Done')
# 关闭连接
cursor.close()
conn.close()