
# 将所有省份的新闻链接合并到一个xlsx文件中

# Province  City  Title  NewsURL  ImageSourceURL
import pandas as pd
import glob
import os

if not os.path.exists('./temp/target'):
    os.makedirs('./temp/target')
# 使用 glob 库获取所有符合模式的文件名
file_pattern = './temp/news_data_*.xlsx'
file_list = glob.glob(file_pattern)

# 初始化一个空的 DataFrame
combined_df = pd.DataFrame()

# 初始化标志变量，用于控制是否写入列名
is_first_file = True

index = 1
# 遍历文件列表，读取每个文件并合并
for file in file_list:
    df = pd.read_excel(file)  # 读取 Excel 文件

    # 确保 DataFrame 包含期望的列
    required_columns = ['Province', 'City', 'Title', 'News URL', 'Image Source URL']
    if not all(col in df.columns for col in required_columns):
        print(f"文件 {file} 不包含所有期望的列：{required_columns}")
        continue

    # 选择所需的列
    df = df[required_columns]

    # 如果是第一个文件，保留列名；否则，不保留列名
    if is_first_file:
        combined_df = df
        is_first_file = False
    else:
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    print(f'{index}: 文件 {file} 已合并')
    index += 1


# 将合并后的 DataFrame 写入一个新的 Excel 文件
combined_df.to_excel('./temp/target/combined_news_data.xlsx', index=False, engine='openpyxl')

print("所有文件已成功合并到 './temp/target/combined_news_data.xlsx' 文件中。")