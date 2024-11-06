'''
此案例为爬取猪八戒网上的开发价格
'''
from lxml import etree
import requests
import re
import openpyxl
import sys
import json
import os

from openpyxl import Workbook

cityname={
        'beijing': '北京市',  # 北京
        'tianjin': '天津市',  # 天津
        'shanghai': '上海市',  # 上海
        'chongqing': '重庆市',  # 重庆
        'haerbin': '哈尔滨市',  # 黑龙江
        'changchun': '长春市',  # 吉林
        'shenyang': '沈阳市',  # 辽宁
        'jinan': '济南市',  # 山东
        'taiyuan': '太原市',  # 山西
        'huhehaote': '呼和浩特市',  # 内蒙古
        'nanjing': '南京市',  # 江苏
        'hangzhou': '杭州市',  # 浙江
        'hefei': '合肥市',  # 安徽
        'fuzhou': '福州市',  # 福建
        'nanchang': '南昌市',  # 江西
        'zhengzhou': '郑州市',  # 河南
        'wuhan': '武汉市',  # 湖北
        'changsha': '长沙市',  # 湖南
        'guangzhou': '广州市',  # 广东
        'nanning': '南宁市',  # 广西
        'haikou': '海口市',  # 海南
        'chengdu': '成都市',  # 四川
        'guiyang': '贵阳市',  # 贵州
        'kunming': '昆明市',  # 云南
        'lasa': '拉萨市',  # 西藏
        'yinchuan': '银川市',  # 宁夏
        'lanzhou': '兰州市',  # 甘肃
        'xining': '西宁市',  # 青海
        'urumqi': '乌鲁木齐市',  # 新疆
        'tangshan': '唐山市',
        'qinhuangdao': '秦皇岛市',
        'handan': '邯郸市',
        'xingtai': '邢台市',
        'baoding': '保定市',
        'zhangjiakou': '张家口市',
        'chengde': '承德市',
        'cangzhou': '沧州市',
        'langfang': '廊坊市',
        'hengshui': '衡水市',
        'datong': '大同市',
        'yangquan': '阳泉市',
        'changzhi': '长治市',
        'jincheng': '晋城市',
        'shuozhou': '朔州市',
        'jinzhong': '晋中市',
        'yuncheng': '运城市',
        'xinzhou': '忻州市',
        'linfen': '临汾市',
        'lvliang': '吕梁市',
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
        'jilin': '吉林市',
        'siping': '四平市',
        'liaoyuan': '辽源市',
        'tonghua': '通化市',
        'baishan': '白山市',
        'songyuan': '松原市',
        'baicheng': '白城市',
        'yanbian': '延边朝鲜族自治州',
        'qiqihar': '齐齐哈尔市',
        'mudanjiang': '牡丹江市',
        'jiamusi': '佳木斯市',
        'daqing': '大庆市',
        'yichun': '伊春市',
        'qitaihe': '七台河市',
        'hegang': '鹤岗市',
        'shuangyashan': '双鸭山市',
        'heihe': '黑河市',
        'suifenhe': '绥芬河市',
        'suihua': '绥化市',
        'daxinganling': '大兴安岭地区',
        'wuxi': '无锡市',
        'xuzhou': '徐州市',
        'changzhou': '常州市',
        'suzhou': '苏州市',
        'nantong': '南通市',
        'lianyungang': '连云港市',
        'huaian': '淮安市',
        'yancheng': '盐城市',
        'yangzhou': '扬州市',
        'zhenjiang': '镇江市',
        'taizhou': '泰州市',
        'suqian': '宿迁市',
        'ningbo': '宁波市',
        'wenzhou': '温州市',
        'jiaxing': '嘉兴市',
        'huzhou': '湖州市',
        'shaoxing': '绍兴市',
        'taizhou': '台州市',
        'jinhua': '金华市',
        'lishui': '丽水市',
        'wuhu': '芜湖市',
        'bengbu': '蚌埠市',
        'huainan': '淮南市',
        'maanshan': '马鞍山市',
        'huizhou': '徽州市',
        'anqing': '安庆市',
        'huangshan': '黄山市',
        'chuzhou': '滁州市',
        'fuyang': '阜阳市',
        'suzhou': '宿州市',
        'luan': '六安市',
        'xuancheng': '宣城市',
        'putian': '莆田市',
        'sanming': '三明市',
        'quanzhou': '泉州市',
        'zhangzhou': '漳州市',
        'nanping': '南平市',
        'longyan': '龙岩市',
        'ningde': '宁德市',
        'jingdezhen': '景德镇市',
        'pingxiang': '萍乡市',
        'jiujiang': '九江市',
        'xinyu': '新余市',
        'yingtan': '鹰潭市',
        'ganzhou': '赣州市',
        'jian': '吉安市',
        'yichun': '宜春市',
        'shangrao': '上饶市',
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
        'sanya': '三亚市',
        'sansha': '三沙市',
        'danzhou': '儋州市',
        'qinghai': '琼海市',
        'wanning': '万宁市',
        'wuzhishan': '五指山市',
        'dongfang': '东方市',
        'lingao': '临高市',
        'changjiang': '昌江黎族自治县',
        'lingao': '陵水黎族自治县',
        'wenchang': '文昌市',
        'xixia': '西沙群岛',
        'baisha': '白沙黎族自治县',
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
        'liupanshui': '六盘水市',
        'zunyi': '遵义市',
        'anshun': '安顺市',
        'tongren': '铜仁市',
        'bijie': '毕节市',
        'qianxinan': '黔西南布依族苗族自治州',
        'qiandongnan': '黔东南苗族侗族自治州',
        'qiannan': '黔南布依族苗族自治州',
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
        'shigatse': '日喀则市',
        'nangqen': '南青县',
        'nagqu': '那曲市',
        'linzhi': '林芝市',
        'qamdo': '昌都市',
        'shizuishan': '石嘴山市',
        'wuzhong': '吴忠市',
        'zhenbeitai': '镇北堡',
        'yingchuan': '盈川县',
        'jiayuguan': '嘉峪关市',
        'jinchang': '金昌市',
        'pingliang': '平凉市',
        'dingxi': '定西市',
        'longnan': '陇南市',
        'qingyang': '庆阳市',
        'haidong': '海东市',
        'haiwei': '海西州',
        'huangnan': '黄南藏族自治州',
        'guoluo': '果洛藏族自治州',
        'yushu': '玉树藏族自治州',
        'haibei': '海北藏族自治州',
        'haixi': '海西蒙古族藏族自治州',
        'kashgar': '喀什市',
        'hetsen': '和田市',
        'hami': '哈密市',
        'kelamayi': '克拉玛依市',
        'aksu': '阿克苏市',
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
    

if __name__ == '__main__':
    if not os.path.exists('./temp'):
        os.makedirs('./temp')
    try:
        cityPath = sys.argv[1]
        with open(cityPath, 'r', encoding='utf-8') as f:
            cityname = json.load(f)
    except:
        print('missing cityPath, use default')
    
    # 创建一个Workbook（工作簿）
    wb = Workbook()
    # 激活工作簿的第一个工作表
    ws = wb.active
    # 给工作表命名（可选）
    ws.title = "纽约时报提及量"
    # 假设我们要添加的数据是一个列表的列表（二维列表），每个子列表代表一行数据
    # 使用append方法，将行数据按行追加写入
    values = ['城市', '起始时间','终止时间','报道次数']
    ws.append(values)

    end=["2014-12-31","2015-12-31","2016-12-31","2017-12-31","2018-12-31","2019-12-31","2020-12-31","2021-12-31","2022-12-31","2023-12-31","2024-12-31"]
    start=["2014-01-01","2015-01-01","2016-01-01","2017-01-01","2018-01-01","2019-01-01","2020-01-01","2021-01-01","2022-01-01","2023-01-01","2024-01-01"]

    items_list = list(cityname.items())
    for key, value in items_list[:]:
    # for key, value in cityname.items():
        for i in range(0,10):
            proxies = {
                'http': 'http://122.189.225.91',
                        'http': 'http://117.40.32.133',
                        'http': 'http://116.169.54.248'
                        # 'http': 'http://101.126.17.117',
                    # 'http': 'http://183.134.101.187','http': 'http://14.204.150.67', 'http': 'http://111.6.43.154', 'http': 'http://47.102.198.154',
                    # 'http': 'http://116.169.54.254', 'http': 'http://123.103.51.22', 'http': 'http://124.236.25.253', 'http': 'http://124.236.25.254',
                    # 'http': 'http://123.121.211.32'
                    }
            url=f'https://www.nytimes.com/search?dropmab=false&endDate={end[i]}&query={key}&sort=newest&startDate={start[i]}'
            header={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36 Edg/126.0.0.0"}
            try:
                response=requests.get(url,headers=header,proxies=proxies)
            except:
                print("request error on:", key, value, 'pass')
                continue

            content=response.text

            tree=etree.HTML(content)
            text=tree.xpath('//*[@id="site-content"]/div/div[1]/div[1]/p/text()')
            if len(text)==0:
                print("没有这个标签")
                continue
            print(text[0])
            # 使用正则表达式匹配第一个数字（包括逗号作为可能的千位分隔符）
            match = re.search(r'\d+(,\d+)*', text[0])

            if match:
                # 提取匹配的文本
                number_with_comma = match.group(0)
                # 如果需要，移除逗号以得到纯数字字符串
                number_without_comma = number_with_comma.replace(',', '')
                print(f"{number_without_comma}")
                values = [f'{value}', f'{start[i]}',f'{end[i]}', number_without_comma]
                ws.append(values)
                wb.save("./temp/纽约时报提及量.xlsx")
            else:
                print("没有这个标签")
    wb.save("./temp/纽约时报提及量.xlsx")