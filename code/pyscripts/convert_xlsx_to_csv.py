import pandas as pd
import sys
import os

def convert_xlsx_to_csv(file_path):
    # 检查文件是否为 .xlsx 文件
    if not file_path.endswith('.xlsx'):
        print("请提供一个 .xlsx 文件")
        return

    # 读取 Excel 文件
    df = pd.read_excel(file_path)

    # 构造 CSV 文件名
    csv_file = os.path.splitext(file_path)[0] + '.csv'

    # 保存为 CSV 文件
    df.to_csv(csv_file, index=False)
    print(f"已将 {file_path} 转换为 {csv_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python convert_xlsx_to_csv.py <文件路径>")
    else:
        file_path = sys.argv[1]
        convert_xlsx_to_csv(file_path)