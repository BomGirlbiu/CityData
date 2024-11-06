
# 使用playwright web自动化库爬取youtube中国城市视频url

from playwright.sync_api import sync_playwright
import pandas as pd
import time
import random
import os

# 城市和省会的映射，键是拼音，值是中文名称
province_capitals = {
    'beijing': '北京市',
    'tianjin': '天津市',
    'shanghai': '上海市',
    'chongqing': '重庆市',
    'haerbin': '哈尔滨市',
    'changchun': '长春市',
    'shenyang': '沈阳市',
    'jinan': '济南市',
    'taiyuan': '太原市',
    'huhehaote': '呼和浩特市',
    'nanjing': '南京市',
    'hangzhou': '杭州市',
    'hefei': '合肥市',
    'fuzhou': '福州市',
    'nanchang': '南昌市',
    'zhengzhou': '郑州市',
    'wuhan': '武汉市',
    'changsha': '长沙市',
    'guangzhou': '广州市',
    'nanning': '南宁市',
    'haikou': '海口市',
    'chengdu': '成都市',
    'guiyang': '贵阳市',
    'kunming': '昆明市',
    'lasa': '拉萨市',
    'yinchuan': '银川市',
    'lanzhou': '兰州市',
    'xining': '西宁市',
    'urumqi': '乌鲁木齐市',
}

other_cities = {
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
    'yichun1': '伊春市',
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
    'taizhou1': '泰州市',
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
    'anqing': '安庆市',
    'huangshan': '黄山市',
    'chuzhou': '滁州市',
    'fuyang': '阜阳市',
    'suzhou1': '宿州市',
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
    'chenzhou': '郴州市',
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
    'yunfu': '云浮市',
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
    'wenchang': '文昌市',
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


def get_youtube_links(page, query):
    """
    获取给定查询词的 YouTube 搜索结果中的前 10 个视频链接及标题
    """
    search_url = f'https://www.youtube.com/results?search_query={query}'
    page.goto(search_url, timeout=60000)  # 增加超时时间到60秒

    # 等待页面加载
    page.wait_for_selector('ytd-video-renderer', timeout=15000)

    # 提取视频链接和标题
    video_data = page.evaluate("""
        () => {
            const data = [];
            const videoElements = document.querySelectorAll('ytd-video-renderer');
            videoElements.forEach((element, index) => {
                if (index < 15) {  // 只获取前 15 个视频
                    const link = element.querySelector('a#video-title').href;
                    const title = element.querySelector('a#video-title').innerText;
                    data.push({ title, link });
                }
            });
            return data;
        }
    """)

    return video_data


def save_to_excel(data, city):
    """
    将所有城市的视频链接及标题保存到 Excel 文件
    """
    # 创建 DataFrame
    df = pd.DataFrame(data, columns=['City Name', 'Video Title', 'Video Link'])

    # 保存到 Excel 文件
    filename = f'./temp/youtube_links_by_{city}_city.xlsx'
    df.to_excel(filename, index=False)
    print(f"Saved video links to {filename}")


def main():
    if not os.path.exists('./temp'):
        os.makedirs('./temp')
    all_data = []

    with sync_playwright() as p:
        # 启动 Chromium 浏览器
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        fg = True

        for city_pinyin, city_name in other_cities.items():
            print(f"Fetching videos for: {city_name} ({city_pinyin})")

            # 获取前 15 个视频链接及标题
            video_data = get_youtube_links(page, city_pinyin)

            # 将城市名称和视频数据添加到数据列表中
            for video in video_data:
                all_data.append([city_name, video['title'], video['link']])

            # 保存到 Excel
            save_to_excel(all_data, city_name)
            all_data = []

            time.sleep(random.uniform(3, 6))  # 同步等待，阻塞整个线程

        # 关闭浏览器
        browser.close()


if __name__ == "__main__":
    main()