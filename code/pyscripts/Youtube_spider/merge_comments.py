import pandas as pd
import glob

def merge_youtube_comments():
    # 获取所有以 youtube_comments_ 开头的 Excel 文件
    all_files = glob.glob('./temp/youtube_comments_*.xlsx')

    # 创建一个空的列表用于存储每个文件的数据
    all_data = []

    # 遍历所有文件并合并数据
    for file in all_files:
        df = pd.read_excel(file)
        all_data.append(df)

    # 使用 pd.concat 合并所有数据
    merged_data = pd.concat(all_data, ignore_index=True)

    # 保存合并后的数据到新的 Excel 文件

    merged_data.to_excel('./temp/target/merged_youtube_comments.xlsx', index=False)
    print("合并完成，文件已保存为 merged_youtube_comments.xlsx")

if __name__ == "__main__":
    merge_youtube_comments()