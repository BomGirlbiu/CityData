# 在google news中爬取中国城市的国际新闻

import requests
from bs4 import BeautifulSoup
import random
import time
from requests.exceptions import RequestException
import pandas as pd
import logging
import os
import sys
import json

if not os.path.exists("./log"):
    os.makedirs("./log")
if not os.path.exists("./temp/target"):
    os.makedirs("./temp/target")
# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(
                            "./log/get_city_news_url.log", encoding='utf-8'),
                        logging.StreamHandler()
                    ])

# 搜索的城市列表
province_city_dict = {
    'beijing': ['beijing'],
    'tianjin': ['tianjin'],
    'shanghai': ['shanghai'],
    'chongqing': ['chongqing'],

    'hebei': ['shijiazhuang', 'tangshan', 'qinhuangdao', 'handan', 'xingtai', 'baoding', 'zhangjiakou', 'chengde1', 'cangzhou', 'langfang', 'hengshui'],
    'shanxi': ['taiyuan', 'datong', 'yangquan', 'changzhi', 'jincheng', 'shuozhou', 'jinzhong', 'yuncheng1', 'xinzhou', 'linfen', 'lvliang'],
    'neimenggu': ['huhehaote', 'baotou', 'wuhai', 'chifeng', 'tongliao', 'ordos', 'hulunbeier', 'bayannaoer', 'wulanchabu', 'xinganmeng', 'xilinguolemeng', 'alashanmeng'],
    'liaoning': ['shenyang', 'dalian', 'anshan', 'fushun', 'benxi', 'dandong', 'jinzhou', 'yingkou', 'fuxin', 'liaoyang', 'panjin', 'tieling', 'chaoyang', 'huludao'],
    'jilin': ['changchun', 'jilin', 'siping', 'liaoyuan', 'tonghua', 'baishan', 'songyuan', 'baicheng', 'yanbian'],
    'heilongjiang': ['haerbin', 'qiqihar', 'mudanjiang', 'jiamusi', 'daqing', 'yichun1', 'qitaihe', 'hegang', 'shuangyashan', 'heihe', 'suifenhe', 'suihua', 'daxinganling'],

    'jiangsu': ['nanjing', 'wuxi', 'xuzhou', 'changzhou', 'suzhou1', 'nantong', 'lianyungang', 'huaian', 'yancheng', 'yangzhou', 'zhenjiang', 'taizhou1', 'suqian'],
    'zhejiang': ['hangzhou', 'ningbo', 'wenzhou', 'jiaxing', 'huzhou', 'shaoxing', 'taizhou', 'jinhua', 'lishui'],
    'anhui': ['hefei', 'wuhu', 'bengbu', 'huainan', 'maanshan', 'huizhou1', 'anqing', 'huangshan', 'chuzhou', 'fuyang', 'suzhou', 'luan', 'xuancheng'],
    'fujian': ['fuzhou', 'xiamen', 'putian', 'sanming', 'quanzhou', 'zhangzhou', 'nanping', 'longyan', 'ningde'],
    'jiangxi': ['nanchang', 'jingdezhen', 'pingxiang', 'jiujiang', 'xinyu', 'yingtan', 'ganzhou', 'jian', 'yichun', 'shangrao'],
    'shandong': ['jinan', 'qingdao', 'zibo', 'zaozhuang', 'jining', 'taian', 'weihai', 'rizhao', 'laiwu', 'dezhou', 'liaocheng', 'binzhou', 'heze'],
    'henan': ['zhengzhou', 'kaifeng', 'luoyang', 'pingdingshan', 'anyang', 'hebi', 'xinxiang', 'jiaozuo', 'xinzheng', 'xuchang', 'luohe', 'nanyang', 'shangqiu', 'xinyang', 'zhoukou', 'zhumadian'],
    'hubei': ['wuhan', 'huangshi', 'shiyan', 'yichang', 'xiangyang', 'ezhou', 'jingmen', 'huanggang', 'xiaogan', 'suizhou', 'enshi', 'qianzhou', 'tianmen', 'shennongjia'],
    'hunan': ['changsha', 'zhuzhou', 'xiangtan', 'hengyang', 'shaoyang', 'yueyang', 'changde', 'zhangjiajie', 'yiyang', 'chengde', 'xianzhou', 'cengdou'],
    'guangdong': ['guangzhou', 'shenzhen', 'zhuhai', 'shantou', 'shaoguan', 'foshan', 'jiangmen', 'zhanjiang', 'maoming', 'zhaoqing', 'huizhou', 'meizhou', 'shantou', 'dongguan', 'zhongshan', 'chaozhou', 'jieyang', 'yuncheng', 'guangdong'],
    'guangxi': ['nanning', 'liuzhou', 'guilin', 'wuzhou', 'beihai', 'fangchenggang', 'qinzhou', 'guigang', 'yulin', 'baise', 'hechi', 'laibin', 'chongzuo'],
    'hainan': ['haikou', 'sanya', 'sansha', 'danzhou', 'qionghai', 'wanning', 'wuzhishan', 'dongfang', 'lingao', 'changjiang', 'lenshui', 'wenchang', 'xixia', 'baisha'],
    'sichuan': ['chengdu', 'zigong', 'panzhihua', 'luzhou', 'deyang', 'mianyang', 'guangyuan', 'suining', 'neijiang', 'leshan', 'nanchong', 'yaan', 'bazhong', 'ziyang', 'yibin', 'chengdu', 'luzhou', 'sichuan'],
    'guizhou': ['guiyang', 'liupanshui', 'zunyi', 'anshun', 'tongren', 'bijie', 'qianxinan', 'qiandongnan', 'qiannan'],
    'yunnan': ['kunming', 'qujing', 'yuxi', 'baoshan', 'zhaotong', 'lijiang', 'puer', 'dehong', 'dali', 'chuxiong', 'nujiang', 'lincang', 'xishuangbanna'],
    'xizang': ['lasa', 'shigatse', 'nangqen', 'nagqu', 'qinghai', 'linzhi', 'qamdo'],

    'ningxia': ['yinchuan', 'shizuishan', 'wuzhong', 'zhenbeitai', 'yingchuan'],
    'gansu': ['lanzhou', 'jiayuguan', 'jinchang', 'pingliang', 'dingxi', 'longnan', 'qingyang', 'lanzhou'],
    'qinghai': ['xining', 'haidong', 'haiwei', 'huangnan', 'guoluo', 'yushu', 'haibei', 'haixi'],
    'xinjiang': ['urumqi', 'kashgar', 'hetsen', 'hami', 'kelamayi', 'aksu', 'hotan', 'korla', 'shache', 'yili', 'altay'],

    'xianggang': ['hongkong'],
    'aomen': ['aomen'],
    'taiwan': ['taipei', 'kaohsiung', 'taichung', 'tainan', 'hualien', 'pingtung', 'keelung', 'taoyuan', 'changhua', 'yunlin', 'chiayi', 'matsu', 'kinmen', 'penghu']
}

# User-Agent 列表
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
]

# 代理池
PROXY_POOL = [
    'http://proxy1.example.com:8000',
    'http://proxy2.example.com:8000',
    'http://proxy3.example.com:8000'
]

# 新闻数据
data = []


def get_random_proxy():
    return random.choice(PROXY_POOL)


def get_random_user_agent():
    return random.choice(USER_AGENTS)


def fetch_news(city, province):
    print(f"\nSearching for city: {city} in {province}")

    # Google News 搜索 URL
    url = f'https://news.google.com/search?q={city}&hl=en-US&gl=US&ceid=US%3Aen'

    # 随机选择代理和 User-Agent
    proxy = get_random_proxy()
    headers = {
        'User-Agent': get_random_user_agent()
    }
    proxies = {
        'http': proxy,
        'https': proxy
    }

    try:
        # 发送请求
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 如果响应状态码不是 200，将抛出异常
        print(f"Status Code: {response.status_code}")  # 打印响应状态码
        # 使用 BeautifulSoup 解析页面
        soup = BeautifulSoup(response.text, 'html.parser')

        # 限制新闻数量 <= 25
        lim = 0

        title = ''
        full_link = ''
        full_src = ''
        # 查找所有 article 标签
        for article in soup.find_all('article'):
            # 查找 article 标签下的 a 标签，class 属性包含 'JtKRv'
            a_tag = article.find('a', class_='JtKRv')
            if a_tag:
                title = a_tag.get_text(strip=True)  # 提取标题文本
                link = a_tag['href']  # 提取链接
                # 拼接完整链接
                full_link = f'https://news.google.com{link[1:]}'
                print(f"Title: {title}")
                print(f"URL: {full_link}")

            # 查找 article 标签下的 img 标签，class 属性包含 'Quavad' 和 'vwBmvb'
            img_tag = article.find('img', class_=['Quavad', 'vwBmvb'])
            if img_tag:
                src = img_tag.get('src')  # 提取 src 属性
                if src.startswith('/'):
                    full_src = f'https://news.google.com{src}'
                else:
                    full_src = src
                print(f"Image Source URL: {full_src}")

            # 将数据添加到列表中
            data.append({
                'Province': province,
                'City': city,
                'Title': title,
                'News URL': full_link,
                'Image Source URL': full_src
            })
            print('-' * 80)
            # 限制新闻数量 <= 20
            lim += 1
            if lim > 20:
                break

    except RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # 等待一段时间，避免过于频繁的请求
    time.sleep(random.uniform(2, 3))  # 等待 5 到 10 秒的随机时间


if __name__ == '__main__':
    try:
        json_path = sys.argv[1]
        # 读取 JSON 文件并加载字典
        with open(json_path, 'r', encoding='utf-8') as f:
            province_city_dict = json.load(f)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        logging.error("missing json_path, use default")

    # 对每个城市执行搜索
    for province, cities in province_city_dict.items():
        # print(f"Province: {province.capitalize()}")
        for city in cities:
            # print(f"  City: {city.capitalize()}")
            fetch_news(city, province)

        # 创建 DataFrame
        df = pd.DataFrame(data)

        # 保存到 Excel 文件
        excel_filename = f'./temp/news_data_{province}.xlsx'
        df.to_excel(excel_filename, index=False, engine='openpyxl')

        # 清空数据以准备下一个省份的数据
        data = []

    print('Data has been written to the respective Excel files.')