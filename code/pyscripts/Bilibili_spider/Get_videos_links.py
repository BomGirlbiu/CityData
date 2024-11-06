# B站城市视频url爬取
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


# 确保日志目录存在
if not os.path.exists("./log"):
    os.makedirs("./log")
if not os.path.exists("./temp"):
    os.makedirs("./temp")
# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(
                            "./log/get_videos_links.log", encoding='utf-8'),
                        logging.StreamHandler()
                    ])

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

city_dict = {
    'beijing': '北京市',
    'tianjin': '天津市',
    'shanghai': '上海市',
    'chongqing': '重庆市',

    'shijiazhuang': '石家庄市',
    'tangshan': '唐山市',
    'qinhuangdao': '秦皇岛市',
    'handan': '邯郸市',
    'xingtai': '邢台市',
    'baoding': '保定市',
    'zhangjiakou': '张家口市',
    'chengde1': '承德市',
    'cangzhou': '沧州市',
    'langfang': '廊坊市',
    'hengshui': '衡水市',

    'taiyuan': '太原市',
    'datong': '大同市',
    'yangquan': '阳泉市',
    'changzhi': '长治市',
    'jincheng': '晋城市',
    'shuozhou': '朔州市',
    'jinzhong': '晋中市',
    'yuncheng1': '运城市',
    'xinzhou': '忻州市',
    'linfen': '临汾市',
    'lvliang': '吕梁市',

    'huhehaote': '呼和浩特市',
    'baotou': '包头市',
    'wuhai': '乌海市',
    'chifeng': '赤峰市',
    'tongliao': '通辽市',
    'ordos': '鄂尔多斯市',
    'hulunbeier': '呼伦贝尔市',
    'bayannaoer': '巴彦淖尔市',
    'wulanchabu': '乌兰察布市',
    'xinganmeng': '兴安盟',
    'xilinguolemeng': '锡林郭勒盟',
    'alashanmeng': '阿拉善盟',

    'shenyang': '沈阳市',
    'dalian': '大连市',
    'anshan': '鞍山市',
    'fushun': '抚顺市',
    'benxi': '本溪市',
    'dandong': '丹东市',
    'jinzhou': '锦州市',
    'yingkou': '营口市',
    'fuxin': '阜新市',
    'liaoyang': '辽阳市',
    'panjin': '盘锦市',
    'tieling': '铁岭市',
    'chaoyang': '朝阳市',
    'huludao': '葫芦岛市',

    'changchun': '长春市',
    'jilin': '吉林市',
    'siping': '四平市',
    'liaoyuan': '辽源市',
    'tonghua': '通化市',
    'baishan': '白山市',
    'songyuan': '松原市',
    'baicheng': '白城市',
    'yanbian': '延边朝鲜族自治州',

    'haerbin': '哈尔滨市',
    'qiqihar': '齐齐哈尔市',
    'mudanjiang': '牡丹江市',
    'jiamusi': '佳木斯市',
    'daqing': '大庆市',
    'yichun1': '伊春市',
    'qitaihe': '七台河市',
    'hegang': '鹤岗市',
    'shuangyashan': '双鸭山市',
    'heihe': '黑河市',
    'suifenhe': '绥芬河市',
    'suihua': '绥化市',
    'daxinganling': '大兴安岭地区',

    'nanjing': '南京市',
    'wuxi': '无锡市',
    'xuzhou': '徐州市',
    'changzhou': '常州市',
    'suzhou1': '苏州市',
    'nantong': '南通市',
    'nantong': '南通市',
    'lianyungang': '连云港市',
    'huaian': '淮安市',
    'yancheng': '盐城市',
    'yangzhou': '扬州市',
    'zhenjiang': '镇江市',
    'taizhou1': '泰州市',
    'suqian': '宿迁市',

    'hangzhou': '杭州市',
    'ningbo': '宁波市',
    'wenzhou': '温州市',
    'jiaxing': '嘉兴市',
    'huzhou': '湖州市',
    'shaoxing': '绍兴市',
    'taizhou': '台州市',
    'jinhua': '金华市',
    'lishui': '丽水市',

    'hefei': '合肥市',
    'wuhu': '芜湖市',
    'bengbu': '蚌埠市',
    'huainan': '淮南市',
    'maanshan': '马鞍山市',
    'huizhou1': '徽州市',
    'anqing': '安庆市',
    'huangshan': '黄山市',
    'chuzhou': '滁州市',
    'fuyang': '阜阳市',
    'suzhou': '宿州市',
    'luan': '六安市',
    'xuancheng': '宣城市',

    'fuzhou': '福州市',
    'xiamen': '厦门市',
    'putian': '莆田市',
    'sanming': '三明市',
    'quanzhou': '泉州市',
    'zhangzhou': '漳州市',
    'nanping': '南平市',
    'longyan': '龙岩市',
    'ningde': '宁德市',

    'nanchang': '南昌市',
    'jingdezhen': '景德镇市',
    'pingxiang': '萍乡市',
    'jiujiang': '九江市',
    'xinyu': '新余市',
    'yingtan': '鹰潭市',
    'ganzhou': '赣州市',
    'jian': '吉安市',
    'yichun': '宜春市',
    'shangrao': '上饶市',

    'jinan': '济南市',
    'qingdao': '青岛市',
    'zibo': '淄博市',
    'zaozhuang': '枣庄市',
    'jining': '济宁市',
    'taian': '泰安市',
    'weihai': '威海市',
    'rizhao': '日照市',
    'laiwu': '莱芜市',
    'dezhou': '德州市',
    'liaocheng': '聊城市',
    'binzhou': '滨州市',
    'heze': '菏泽市',

    'zhengzhou': '郑州市',
    'kaifeng': '开封市',
    'luoyang': '洛阳市',
    'pingdingshan': '平顶山市',
    'anyang': '安阳市',
    'hebi': '鹤壁市',
    'xinxiang': '新乡市',
    'jiaozuo': '焦作市',
    'xinzheng': '新郑市',
    'xuchang': '许昌市',
    'luohe': '漯河市',
    'nanyang': '南阳市',
    'xinyang': '信阳市',
    'zhoukou': '周口市',
    'zhumadian': '驻马店市',

    'wuhan': '武汉市',
    'huangshi': '黄石市',
    'shiyan': '十堰市',
    'yichang': '宜昌市',
    'xiangyang': '襄阳市',
    'ezhou': '鄂州市',
    'jingmen': '荆门市',
    'huanggang': '黄冈市',
    'xiaogan': '孝感市',
    'suizhou': '随州市',
    'enshi': '恩施土家族苗族自治州',
    'qianzhou': '潜江市',
    'tianmen': '天门市',
    'shennongjia': '神农架林区',

    'changsha': '长沙市',
    'zhuzhou': '株洲市',
    'xiangtan': '湘潭市',
    'hengyang': '衡阳市',
    'shaoyang': '邵阳市',
    'yueyang': '岳阳市',
    'changde': '常德市',
    'zhangjiajie': '张家界市',
    'yiyang': '益阳市',
    'chengde': '郴州市',
    'xianzhou': '湘西土家族苗族自治州',
    'cengdou': '岳阳楼区',

    'guangzhou': '广州市',
    'shenzhen': '深圳市',
    'zhuhai': '珠海市',
    'shantou': '汕头市',
    'shaoguan': '韶关市',
    'foshan': '佛山市',
    'jiangmen': '江门市',
    'zhanjiang': '湛江市',
    'maoming': '茂名市',
    'zhaoqing': '肇庆市',
    'huizhou': '惠州市',
    'meizhou': '梅州市',
    'dongguan': '东莞市',
    'zhongshan': '中山市',
    'chaozhou': '潮州市',
    'jieyang': '揭阳市',
    'yuncheng': '云浮市',
    'guangdong': '广东省',

    'nanning': '南宁市',
    'liuzhou': '柳州市',
    'guilin': '桂林市',
    'wuzhou': '梧州市',
    'beihai': '北海市',
    'fangchenggang': '防城港市',
    'qinzhou': '钦州市',
    'guigang': '贵港市',
    'yulin': '玉林市',
    'baise': '百色市',
    'hechi': '河池市',
    'laibin': '来宾市',
    'chongzuo': '崇左市',

    'haikou': '海口市',
    'sanya': '三亚市',
    'sansha': '三沙市',
    'danzhou': '儋州市',
    'qionghai': '琼海市',
    'wanning': '万宁市',
    'wuzhishan': '五指山市',
    'dongfang': '东方市',
    'lingao': '临高市',
    'changjiang': '昌江黎族自治县',
    'lenshui': '陵水黎族自治县',
    'wenchang': '文昌市',
    'xixia': '西沙群岛',
    'baisha': '白沙黎族自治县',

    'chengdu': '成都市',
    'zigong': '自贡市',
    'panzhihua': '攀枝花市',
    'luzhou': '泸州市',
    'deyang': '德阳市',
    'mianyang': '绵阳市',
    'guangyuan': '广元市',
    'suining': '遂宁市',
    'neijiang': '内江市',
    'leshan': '乐山市',
    'nanchong': '南充市',
    'yaan': '雅安市',
    'bazhong': '巴中市',
    'ziyang': '资阳市',
    'yibin': '宜宾市',

    'guiyang': '贵阳市',
    'liupanshui': '六盘水市',
    'zunyi': '遵义市',
    'anshun': '安顺市',
    'tongren': '铜仁市',
    'bijie': '毕节市',
    'qianxinan': '黔西南布依族苗族自治州',
    'qiandongnan': '黔东南苗族侗族自治州',
    'qiannan': '黔南布依族苗族自治州',

    'kunming': '昆明市',
    'qujing': '曲靖市',
    'yuxi': '玉溪市',
    'baoshan': '保山市',
    'zhaotong': '昭通市',
    'lijiang': '丽江市',
    'puer': '普洱市',
    'dehong': '德宏傣族景颇族自治州',
    'dali': '大理白族自治州',
    'chuxiong': '楚雄彝族自治州',
    'nujiang': '怒江傈僳族自治州',
    'lincang': '临沧市',
    'xishuangbanna': '西双版纳傣族自治州',

    'lasa': '拉萨市',
    'shigatse': '日喀则市',
    'nangqen': '南青县',
    'nagqu': '那曲市',
    'qinghai': '青海市',
    'linzhi': '林芝市',
    'qamdo': '昌都市',

    'yinchuan': '银川市',
    'shizuishan': '石嘴山市',
    'wuzhong': '吴忠市',
    'zhenbeitai': '镇北堡',
    'yingchuan': '盈川县',

    'lanzhou': '兰州市',
    'jiayuguan': '嘉峪关市',
    'jinchang': '金昌市',
    'pingliang': '平凉市',
    'dingxi': '定西市',
    'longnan': '陇南市',
    'qingyang': '庆阳市',

    'xining': '西宁市',
    'haidong': '海东市',
    'haiwei': '海西州',
    'huangnan': '黄南藏族自治州',
    'guoluo': '果洛藏族自治州',
    'yushu': '玉树藏族自治州',
    'haibei': '海北藏族自治州',
    'haixi': '海西蒙古族藏族自治州',

    'urumqi': '乌鲁木齐市',
    'kashgar': '喀什市',
    'hetsen': '和田市',
    'hami': '哈密市',
    'kelamayi': '克拉玛依市',
    'aksu': '阿克苏市',
    'hotan': '和田市',
    'korla': '库尔勒市',
    'shache': '莎车市',
    'yili': '伊犁哈萨克自治州',
    'altay': '阿勒泰地区',

    'hongkong': '香港',
    'aomen': '澳门',
    'taipei': '台北市',
    'kaohsiung': '高雄市',
    'taichung': '台中市',
    'tainan': '台南市',
    'hualien': '花莲市',
    'pingtung': '屏东县',
    'keelung': '基隆市',
    'taoyuan': '桃园市',
    'changhua': '彰化市',
    'yunlin': '云林县',
    'chiayi': '嘉义市',
    'matsu': '马祖',
    'kinmen': '金门',
    'penghu': '澎湖'
}

# User-Agent 列表
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
]

data = []


def get_random_user_agent():
    return random.choice(USER_AGENTS)


def fetch_news_videos(city):
    logging.info(f"Searching for city: {city}")
    url = f'https://search.bilibili.com/all?keyword={city}'
    headers = {
        'User-Agent': get_random_user_agent()
    }

    try:
        # 发送请求
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 如果响应状态码不是 200，将抛出异常
        logging.info(f"Status Code: {response.status_code}")  # 打印响应状态码
        # 使用 BeautifulSoup 解析页面
        soup = BeautifulSoup(response.text, 'html.parser')

        # 限制新闻数量 <= 25
        lim = 1

        full_url = ''
        full_src = ''
        full_alt = ''
        div_tags = soup.find_all(
            'div', class_='bili-video-card__wrap __scale-wrap')
        for div in div_tags:
            a_tag = div.find('a')
            if a_tag and 'href' in a_tag.attrs:
                href = 'https:' + a_tag['href']
                full_url = href

            picture_tag = div.find('picture')
            if picture_tag:
                img_tag = picture_tag.find('img')
                if img_tag:
                    src = 'https:' + img_tag.get('src', 'No src found')
                    alt = img_tag.get('alt', 'No alt found')
                    full_src = src
                    full_alt = alt

            # 将数据添加到列表中
            if full_url.startswith("https://"):
                logging.info(f"{lim}:视频链接: {full_url}")
                logging.info(f"{lim}:图片链接: {full_src}, 描述: {full_alt}")
                data.append({
                    'City': city,
                    'videoImageURL': full_src,
                    'videoURL': full_url,
                    'videoAlt': full_alt
                })
                # 限制新闻数量 <= 10
                lim += 1
                if lim > 10:
                    break

    except RequestException as e:
        logging.error(f"Request failed: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    # 等待一段时间，避免过于频繁的请求
    time.sleep(random.uniform(1, 3))  # 等待 5 到 10 秒的随机时间


# 对每个城市执行搜索
if __name__ == '__main__':
    # 获取当前文件的目录
    try:
        json_path = sys.argv[1]
        # 读取 JSON 文件并加载字典
        with open(json_path, 'r', encoding='utf-8') as f:
            province_city_dict = json.load(f)
    except IndexError:
        logging.error("missing json_path, use default")

    for province, cities in province_city_dict.items():
        for c in cities:
            def remove_city_suffix(city_name):
                # 判断字符串是否以 "市" 结尾
                if city_name.endswith("市"):
                    # 去掉最后一个字符 "市"
                    return city_name[:-1]
                return city_name

            city = city_dict.get(c)
            city = remove_city_suffix(str(city))
            if city is not None:
                fetch_news_videos(city)

        # 创建 DataFrame
        df = pd.DataFrame(data)

        # 保存到 Excel 文件
        excel_filename = f'./temp/news_videos_{province}.xlsx'
        df.to_excel(excel_filename, index=False, engine='openpyxl')

        # 清空数据以准备下一个省份的数据
        data = []
    logging.info('Data has been written to the respective Excel files.')
