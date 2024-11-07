# 爬取城市图片
import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
from requests import RequestException
import time
import json
import os


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

province_dict = {
    'beijing': '北京市',
    'tianjin': '天津市',
    'shanghai': '上海市',
    'chongqing': '重庆市',

    'hebei': '河北省',
    'shanxi': '山西省',
    'neimenggu': '内蒙古自治区',
    'liaoning': '辽宁省',
    'jilin': '吉林省',
    'heilongjiang': '黑龙江省',

    'jiangsu': '江苏省',
    'zhejiang': '浙江省',
    'anhui': '安徽省',
    'fujian': '福建省',
    'jiangxi': '江西省',
    'shandong': '山东省',
    'henan': '河南省',
    'hubei': '湖北省',
    'hunan': '湖南省',
    'guangdong': '广东省',
    'guangxi': '广西壮族自治区',
    'hainan': '海南省',
    'sichuan': '四川省',
    'guizhou': '贵州省',
    'yunnan': '云南省',
    'xizang': '西藏自治区',

    'ningxia': '宁夏回族自治区',
    'gansu': '甘肃省',
    'qinghai': '青海省',
    'xinjiang': '新疆维吾尔自治区',

    'xianggang': '香港特别行政区',
    'aomen': '澳门特别行政区',
    'taiwan': '台湾省'
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


def fetch_img(city, province):
    try:
        print(f"\nSearching for city: {city} in {province}")
        headers = {
            "cookie":'sajssdk_2015_cross_new_user=1; FZ_STROAGE.vcg.com=eyJTRUVTSU9OSUQiOiI1ZjJjNTFhMjYxY2NjYmNmIiwiU0VFU0lPTkRBVEUiOjE3MjM4MDc5NTkwNDh9; ARK_ID=undefined; _c_WBKFRo=P1Sa30R6xhOKBMqEdKsQJ2qmg6yMY07jWJVKtdsF; clientIp=58.20.74.75; uuid=ce2d551e-e5fd-42a2-b43c-6a845c13e6e0; Hm_lvt_5fd2e010217c332a79f6f3c527df12e9=1723807978,1723808015,1723810677,1723810721; HMACCOUNT=8B90982D965CE303; api_token=ST-577-9a21b0e15477086ecb063e43dcc043484; name=15673127607; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22d13b1f2d14ffe9b03eede88f9fd175486%22%2C%22first_id%22%3A%221915adb72501411-0f1ed516678613-26001f51-1821369-1915adb725120c6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221915adb72501411-0f1ed516678613-26001f51-1821369-1915adb725120c6%22%7D; fingerprint=9a54fa399638edbb55767431d35207a3; acw_tc=2760829517238145249782323e90a2ded42ff0c7923ea42f78797ce85d5c09; _fp_=eyJpcCI6IjU4LjIwLjc0Ljc1IiwiZnAiOiI5YTU0ZmEzOTk2MzhlZGJiNTU3Njc0MzFkMzUyMDdhMyIsImhzIjoiJDJhJDA4JFFmMHNDU2x3OFl5NmZHZ2V4azlhTXVVUC51Z2xCQUhJaUhOY3hkcmkzaVppMjVCaXRlZTVTIn0%3D; Hm_lpvt_5fd2e010217c332a79f6f3c527df12e9=1723814742; ssxmod_itna=YqjxyDuGDtitdGKe0Lx0PDQ92eewOGEqRD+AE27+fqGXtG8IDnqD=GFDK40EEkAP7fGODQQ0GcRYdq7Ql4uhFdFQAaqeF2nb7voDU4i8DCdM3tD485GwD0eG+DD4DW9x03DoxGYlAx0bCy6Hs26KDpxGrDlKDRx07KK5DbxDaDGaCiePK2cKDhxDCDiv+GFYDixianhxDBhxje60k7Di32EH7Q8Aw++Gz1nrCD75Dux0H0CQvG+jR7DAzVKC66jI+340OD0FmB=IwFivGlhF6aDrdqD2e4=04TmW5Ynhq8+DxjXteLXz55eXgxLSreNntq+hT2hUYD==; ssxmod_itna2=YqjxyDuGDtitdGKe0Lx0PDQ92eewOGEqRD+AE274xA=9N4D/QSSDFE72KtKksXqG87x7QQ2DjKD20YD=',
            'User-Agent': get_random_user_agent()
        }
        # 设置目标URL
        url = f"https://www.vcg.com/creative-image/{city_dict[city]}/"
        print(url)

        # 发送GET请求获取网页内容
        response = requests.get(url, headers=headers, timeout=10)
        # print(response.content)
        # 检查请求是否成功
        if response.status_code == 200:
            # 解析网页内容
            soup = BeautifulSoup(response.content, 'html.parser')
            # 查找所有带有 class="galleryItem" 的 figure 标签
            figures = soup.find_all('figure', class_='galleryItem')

            lim = 0
            # 提取每个 figure 标签中的 img 标签的 src 属性
            for figure in figures:
                img = figure.find('img')  # 通常 src 属性在 img 标签中
                if img and 'data-src' in img.attrs:
                    src = img['data-src']
                    # 拼接完整的 URL
                    full_url = "https:" + src if src.startswith('//') else src
                    print(f"The src attribute of a galleryItem: {full_url}")
                    data.append({
                        'City': city,
                        'Province': province,
                        'Image Source URL': full_url
                    })
                    lim += 1
                    if lim > 15:
                        break
                # else:
                #     print("No img tag with src attribute found within the figure.")
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
        print('')
    except RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # 等待一段时间，避免过于频繁的请求
    time.sleep(random.uniform(2, 5))  # 等待 10 到 15 秒的随机时间


if __name__ == '__main__':
    if not os.path.exists('./temp'):
        os.makedirs('./temp')
    try:
        jsonPath = './province_city_dict.json'
        with open(jsonPath, 'r', encoding='utf-8') as f:
            province_city_dict = json.load(f)
    except Exception as e:
        print('missing json file, use default dict')

    for province, cities in province_city_dict.items():
        # print(f"Province: {province.capitalize()}")
        for city in cities:
            # print(f"  City: {city.capitalize()}")
            fetch_img(city, province)

        # 创建 DataFrame
        df = pd.DataFrame(data)

        # 保存到 Excel 文件
        excel_filename = f'./temp/news_img_{province}.xlsx'
        df.to_excel(excel_filename, index=False, engine='openpyxl')

        # 清空数据以准备下一个省份的数据
        data = []

    print('Data has been written to the respective Excel files.')