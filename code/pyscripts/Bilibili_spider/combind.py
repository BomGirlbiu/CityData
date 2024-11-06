import pandas as pd
import glob
import sys
import os


if __name__ == '__main__':
    # Ensure the ./temp path exists
    if not os.path.exists('./temp/target'):
        os.makedirs('./temp/target')
    ctype = 0
    try:
        ctype = sys.argv[1]
    except:
        pass
    if ctype == 0:
        file_list = glob.glob('./temp/news_videos_*.xlsx')
        combined_file = './temp/target/combined_news_videos.xlsx'
    else:
        file_list = glob.glob('./temp/*_comments.xlsx')
        combined_file = './temp/target/combined_comments.xlsx'

    # 创建一个空的DataFrame用于存储合并后的数据
    combined_df = pd.DataFrame()

    for file in file_list:
        df = pd.read_excel(file)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    # 将合并后的DataFrame保存到一个新的xlsx文件中
    combined_df.to_excel(combined_file,
                         index=False, engine='openpyxl')

    print("所有文件已成功合并到 %s" % combined_file)
