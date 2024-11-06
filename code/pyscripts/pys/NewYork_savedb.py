import pandas as pd
import pymysql
import sys

def insert_data_to_db(db_name, user, password):
    try:
        # 读取Excel文件
        df = pd.read_excel('./temp/纽约时报提及量.xlsx')

        # 连接到数据库
        connection = pymysql.connect(
            host='localhost',
            database=db_name,
            user=user,
            password=password
        )

        cursor = connection.cursor()

        # 插入数据
        for index, row in df.iterrows():
            sql_insert_query = """INSERT INTO newyork_counts (city, start_date, end_date, insert_date, count)
                                  VALUES (%s, %s, %s, NOW(), %s)"""
            cursor.execute(sql_insert_query, (row['城市'], row['起始时间'], row['终止时间'], row['报道次数']))

        connection.commit()
        print("数据插入成功")

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("用法: python script.py <数据库名称> <用户名> <密码>")
    else:
        db_name = sys.argv[1]
        user = sys.argv[2]
        password = sys.argv[3]
        insert_data_to_db(db_name, user, password)
