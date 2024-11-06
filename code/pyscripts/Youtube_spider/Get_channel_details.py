
# 使用Google api 爬取youtube具体频道的信息

import requests
import pandas as pd
from channel_names import channel_name


api_key = ''  # 替换为实际的 API 密钥


def get_channel_info(api_key, channel_id, city):
    search_url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&id={channel_id}&key={api_key}'
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            item = data['items'][0]
            snippet = item['snippet']
            statistics = item['statistics']
            print(f'{city} is ok')
            return {
                'city': city,
                'title': snippet['title'],
                'description': snippet['description'],
                'publishedAt': snippet['publishedAt'],
                'subscriberCount': statistics.get('subscriberCount', 'N/A'),
                'videoCount': statistics.get('videoCount', 'N/A'),
                'viewCount': statistics.get('viewCount', 'N/A')
            }
        else:
            print("No channel found.")
            return None
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        return None


channel_infos = []
for city, channel_id in channel_name.items():
    channel_data = get_channel_info(api_key, channel_id, city)
    if channel_data:
        channel_infos.append(channel_data)
    print('')

# 创建数据框（DataFrame）
df = pd.DataFrame(channel_infos)

# 保存数据框到 Excel 文件
excel_file = 'channels_info.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f"Channel information has been saved to {excel_file}.")