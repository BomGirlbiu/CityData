
# 通过频道名查找频道id

import requests

def get_channel_id(api_key, username):
    """
    获取 YouTube 频道 ID 通过用户名
    参数:
    api_key (str): YouTube Data API 的 API 密钥
    username (str): YouTube 频道的用户名
    返回:
    str: 频道 ID，如果没有找到频道则返回 None
    """
    # 构建请求 URL
    search_url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet&forUsername={username}&key={api_key}'

    try:
        # 发送请求并获取响应
        response = requests.get(search_url)
        response.raise_for_status()  # 如果响应状态码不是 200，会抛出 HTTPError
        data = response.json()

        # 打印响应内容以调试
        print("API Response:", data)

        # 检查 'items' 键是否存在
        if 'items' in data and len(data['items']) > 0:
            channel_info = data['items'][0]
            channel_id = channel_info['id']
            return channel_id
        else:
            print("No channel found.")
            return None

    except requests.exceptions.RequestException as e:
        # 捕获所有请求异常（如网络问题、无效的 URL 等）
        print("Request error:", e)
        return None
