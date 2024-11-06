
# 使用google api获取频道下的视频id

import requests
import pandas as pd

province_city_dict = {
    'beijing': ['beijing'],
    'tianjin': ['tianjin'],
    'shanghai': ['shanghai'],
    'chongqing': ['chongqing'],

    'hebei': ['shijiazhuang', 'tangshan', 'qinhuangdao', 'handan', 'xingtai', 'baoding', 'zhangjiakou', 'chengde', 'cangzhou', 'langfang', 'hengshui'],
    'shanxi': ['taiyuan', 'datong', 'yangquan', 'changzhi', 'jincheng', 'shuozhou', 'jinzhong', 'yuncheng', 'xinzhou', 'linfen', 'lvliang'],
    'neimenggu': ['huhehaote', 'baotou', 'wuhai', 'chifeng', 'tongliao', 'ordos', 'hulunbeier', 'bayannaoer', 'wulanchabu', 'xinganmeng', 'xilinguolemeng', 'alashanmeng'],
    'liaoning': ['shenyang', 'dalian', 'anshan', 'fushun', 'benxi', 'dandong', 'jinzhou', 'yingkou', 'fuxin', 'liaoyang', 'panjin', 'tieling', 'chaoyang', 'huludao'],
    'jilin': ['changchun', 'jilin', 'siping', 'liaoyuan', 'tonghua', 'baishan', 'songyuan', 'baicheng', 'yanbian'],
    'heilongjiang': ['haerbin', 'qiqihar', 'mudanjiang', 'jiamusi', 'daqing', 'yichun', 'qitaihe', 'hegang', 'shuangyashan', 'heihe', 'suifenhe', 'suihua', 'daxinganling'],

    'jiangsu': ['nanjing', 'wuxi', 'xuzhou', 'changzhou', 'suzhou', 'nantong', 'lianyungang', 'huaian', 'yancheng', 'yangzhou', 'zhenjiang', 'taizhou', 'suqian'],
    'zhejiang': ['hangzhou', 'ningbo', 'wenzhou', 'jiaxing', 'huzhou', 'shaoxing', 'taizhou', 'jinhua', 'lishui'],
    'anhui': ['hefei', 'wuhu', 'bengbu', 'huainan', 'maanshan', 'huizhou', 'anqing', 'huangshan', 'chuzhou', 'fuyang', 'suzhou', 'luan', 'xuancheng'],
    'fujian': ['fuzhou', 'xiamen', 'putian', 'sanming', 'quanzhou', 'zhangzhou', 'nanping', 'longyan', 'ningde'],
    'jiangxi': ['nanchang', 'jingdezhen', 'pingxiang', 'jiujiang', 'xinyu', 'yingtan', 'ganzhou', 'jian', 'yichun', 'shangrao'],
    'shandong': ['jinan', 'qingdao', 'zibo', 'zaozhuang', 'jining', 'taian', 'weihai', 'rizhao', 'laiwu', 'dezhou', 'liaocheng', 'binzhou', 'heze'],
    'henan': ['zhengzhou', 'kaifeng', 'luoyang', 'pingdingshan', 'anyang', 'hebi', 'xinxiang', 'jiaozuo', 'xinzheng', 'xuchang', 'luohe', 'nanyang', 'shangqiu', 'xinyang', 'zhoukou', 'zhumadian'],
    'hubei': ['wuhan', 'huangshi', 'shiyan', 'yichang', 'xiangyang', 'ezhou', 'jingmen', 'huanggang', 'xiaogan', 'suizhou', 'enshi', 'qianzhou', 'tianmen', 'shennongjia'],
    'hunan': ['changsha', 'zhuzhou', 'xiangtan', 'hengyang', 'shaoyang', 'yueyang', 'changde', 'zhangjiajie', 'yiyang', 'chengde', 'xianzhou', 'cengdou'],
    'guangdong': ['guangzhou', 'shenzhen', 'zhuhai', 'shantou', 'shaoguan', 'foshan', 'jiangmen', 'zhanjiang', 'maoming', 'zhaoqing', 'huizhou', 'meizhou', 'shantou', 'dongguan', 'zhongshan', 'chaozhou', 'jieyang', 'yuncheng', 'guangdong'],
    'guangxi': ['nanning', 'liuzhou', 'guilin', 'wuzhou', 'beihai', 'fangchenggang', 'qinzhou', 'guigang', 'yulin', 'baise', 'hechi', 'laibin', 'chongzuo'],
    'hainan': ['haikou', 'sanya', 'sansha', 'danzhou', 'qinghai', 'wanning', 'wuzhishan', 'dongfang', 'lingao', 'changjiang', 'lingao', 'wenchang', 'xixia', 'baisha'],
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

# 设置 API 密钥和频道 ID
api_key = ''  # 替换为实际 API 密钥
# 该id为Walk East的channel_id
channel_id = ''  # 替换为实际的频道 ID


# 函数获取频道下的视频 ID
def get_video_ids(api_key, channel_id, query, max_results=10):
    video_ids = []
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'id',
        'channelId': channel_id,
        'q': query,
        'maxResults': max_results,  # 设置为最大结果数
        'order': 'date',  # 排序方式
        'key': api_key
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if 'items' in data:
        for item in data['items']:
            video_id = item['id'].get('videoId')
            if video_id:
                video_ids.append(video_id)

    return video_ids


# 对每个城市执行搜索
for province, cities in province_city_dict.items():
    # print(f"Province: {province.capitalize()}")
    for city in cities:
        # 获取前 10 条视频 ID
        video_ids = get_video_ids(api_key, channel_id, city, max_results=10)
        if len(video_ids) > 0:
            data = []
            print(city)
            # 打印视频 ID
            print("Video IDs:", video_ids)
            for video_id in video_ids:
                data.append({
                    'Video_id': video_id,
                    'City': city
                })
                # 创建 DataFrame
            df = pd.DataFrame(data)

            # 保存到 Excel 文件
            excel_filename = f'city_video_id.xlsx'
            df.to_excel(excel_filename, index=False, engine='openpyxl')
