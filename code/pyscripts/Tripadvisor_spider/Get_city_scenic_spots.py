
# 爬取Tripadvisor中国网站

import pandas as pd
from playwright.sync_api import sync_playwright
import os

Tripadvisor_province_capitals = {
    '北京市': 'https://www.tripadvisor.cn/Attractions-g294212-Activities-Beijing.html',
    '天津市': 'https://www.tripadvisor.cn/Attractions-g311293-Activities-Tianjin.html',
    '上海市': 'https://www.tripadvisor.cn/Attractions-g308272-Activities-Shanghai.html',
    '重庆市': 'https://www.tripadvisor.cn/Attractions-g294213-Activities-Chongqing.html',
    '哈尔滨市': 'https://www.tripadvisor.cn/Attractions-g297433-Activities-Harbin_Heilongjiang.html',
    '长春市': 'https://www.tripadvisor.cn/Attractions-g297448-Activities-Changchun_Jilin.html',
    '沈阳市': 'https://www.tripadvisor.cn/Attractions-g297454-Activities-Shenyang_Liaoning.html',
    '济南市': 'https://www.tripadvisor.cn/Attractions-g297457-Activities-Jinan_Shandong.html',
    '太原市': 'https://www.tripadvisor.cn/Attractions-g317093-Activities-Taiyuan_Shanxi.html',
    '呼和浩特市': 'https://www.tripadvisor.cn/Attractions-g297440-Activities-Hohhot_Inner_Mongolia.html',
    '南京市': 'https://www.tripadvisor.cn/Attractions-g294220-Activities-Nanjing_Jiangsu.html',
    '杭州市': 'https://www.tripadvisor.cn/Attractions-g298559-Activities-Hangzhou_Zhejiang.html',
    '合肥市': 'https://www.tripadvisor.cn/Attractions-g297403-Activities-Hefei_Anhui.html',
    '福州市': 'https://www.tripadvisor.cn/Attractions-g297405-Activities-Fuzhou_Fujian.html',
    '南昌市': 'https://www.tripadvisor.cn/Attractions-g297446-Activities-Nanchang_Jiangxi.html',
    '郑州市': 'https://www.tripadvisor.cn/Attractions-g297435-Activities-Zhengzhou_Henan.html',
    '武汉市': 'https://www.tripadvisor.cn/Attractions-g297437-Activities-Wuhan_Hubei.html',
    '长沙市': 'https://www.tripadvisor.cn/Attractions-g494932-Activities-Changsha_Hunan.html',
    '广州市': 'https://www.tripadvisor.cn/Attractions-g298555-Activities-Guangzhou_Guangdong.html',
    '南宁市': 'https://www.tripadvisor.cn/Attractions-g317092-Activities-Nanning_Guangxi.html',
    '海口市': 'https://www.tripadvisor.cn/Attractions-g297425-Activities-Haikou_Hainan.html',
    '成都市': 'https://www.tripadvisor.cn/Attractions-g297463-Activities-Chengdu_Sichuan.html',
    '贵阳市': 'https://www.tripadvisor.cn/Attractions-g317090-Activities-Guiyang_Guizhou.html',
    '昆明市': 'https://www.tripadvisor.cn/Attractions-g298558-Activities-Kunming_Yunnan.html',
    '拉萨市': 'https://www.tripadvisor.cn/Attractions-g294223-Activities-Lhasa_Tibet.html',
    '银川市': 'https://www.tripadvisor.cn/Attractions-g494938-Activities-Yinchuan_Ningxia.html',
    '兰州市': 'https://www.tripadvisor.cn/Attractions-g297409-Activities-Lanzhou_Gansu.html',
    '西宁市': 'https://www.tripadvisor.cn/Attractions-g494940-Activities-Xining_Qinghai.html',
    '乌鲁木齐市': 'https://www.tripadvisor.cn/Attractions-g297466-Activities-Urumqi_Xinjiang_Uygur.html',
    '香港': 'https://www.tripadvisor.cn/Attractions-g294217-Activities-Hong_Kong.html',
    '澳门': 'https://www.tripadvisor.cn/Attractions-g664891-Activities-Macau.html',
    '台北市': ''
}

Tripadvisor_other_cities = {
    '唐山市': 'https://www.tripadvisor.cn/Attractions-g659916-Activities-Tangshan_Hebei.html',
    '秦皇岛市': 'https://www.tripadvisor.cn/Attractions-g297430-Activities-Qinhuangdao_Hebei.html',
    '邯郸市': 'https://www.tripadvisor.cn/Attractions-g1017003-Activities-Handan_Hebei.html',
    '邢台市': '',
    '保定市': 'https://www.tripadvisor.cn/Attractions-g658402-Activities-Baoding_Hebei.html',
    '张家口市': '',
    '承德市': 'https://www.tripadvisor.cn/Attractions-g303721-Activities-Chengde_Hebei.html',
    '沧州市': '',
    '廊坊市': 'https://www.tripadvisor.cn/Attractions-g635518-Activities-Langfang_Hebei.html',
    '衡水市': '',
    '大同市': 'https://www.tripadvisor.cn/Attractions-g297461-Activities-Datong_Shanxi.html',
    '阳泉市': 'https://www.tripadvisor.cn/Attractions-g1016992-Activities-Yangquan_Shanxi.html',
    '长治市': '',
    '晋城市': 'https://www.tripadvisor.cn/Attractions-g659919-Activities-Jincheng_Shanxi.html',
    '朔州市': 'https://www.tripadvisor.cn/Attractions-g1016991-Activities-Shuozhou_Shanxi.html',
    '晋中市': 'https://www.tripadvisor.cn/Attractions-g1016995-Activities-Jinzhong_Shanxi.html',
    '运城市': 'https://www.tripadvisor.cn/Attractions-g678438-Activities-Yuncheng_Shanxi.html',
    '忻州市': 'https://www.tripadvisor.cn/Attractions-g1016994-Activities-Xinzhou_Shanxi.html',
    '临汾市': 'https://www.tripadvisor.cn/Attractions-g1016996-Activities-Linfen_Shanxi.html',
    '吕梁市': '',
    '包头市': 'https://www.tripadvisor.cn/Attractions-g580103-Activities-Baotou_Inner_Mongolia.html',
    '乌海市': '',
    '赤峰市': 'https://www.tripadvisor.cn/Attractions-g1016964-Activities-Chifeng_Inner_Mongolia.html',
    '通辽市': '',
    '鄂尔多斯市': 'https://www.tripadvisor.cn/Attractions-g1016967-Activities-Ordos_Inner_Mongolia.html',
    '呼伦贝尔市': 'https://www.tripadvisor.cn/Attractions-g1016966-Activities-Hulunbuir_Inner_Mongolia.html',
    '巴彦淖尔市': '',
    '乌兰察布市': 'https://www.tripadvisor.cn/Attractions-g1016968-Activities-Ulaan_Chab_Inner_Mongolia.html',
    '兴安盟': '',
    '锡林郭勒盟': '',
    '阿拉善盟': '',
    '大连市': 'https://www.tripadvisor.cn/Attractions-g297452-Activities-Dalian_Liaoning.html',
    '鞍山市': 'https://www.tripadvisor.cn/Attractions-g297451-Activities-Anshan_Liaoning.html',
    '抚顺市': '',
    '本溪市': '',
    '丹东市': 'https://www.tripadvisor.cn/Attractions-g303754-Activities-Dandong_Liaoning.html',
    '锦州市': 'https://www.tripadvisor.cn/Attractions-g616024-Activities-Jinzhou_Liaoning.html',
    '营口市': '',
    '阜新市': '',
    '辽阳市': '',
    '盘锦市': '',
    '铁岭市': '',
    '朝阳市': 'https://www.tripadvisor.cn/Attractions-g297449-Activities-Chaoyang_Liaoning.html',
    '葫芦岛市': '',
    '吉林市': 'https://www.tripadvisor.cn/Attractions-g494936-Activities-Jilin_Jilin.html',
    '四平市': 'https://www.tripadvisor.cn/Attractions-g1017067-Activities-Siping_Jilin.html',
    '辽源市': '',
    '通化市': '',
    '白山市': '',
    '松原市': '',
    '白城市': '',
    '延边朝鲜族自治州': 'https://www.tripadvisor.cn/Attractions-g644037-Activities-Yanji_Yanbian_Korean_Autonomous_Prefecture_Jilin.html',
    '齐齐哈尔市': 'https://www.tripadvisor.cn/Attractions-g798009-Activities-Qiqihar_Heilongjiang.html',
    '牡丹江市': 'https://www.tripadvisor.cn/Attractions-g494929-Activities-Mudanjiang_Heilongjiang.html',
    '佳木斯市': 'https://www.tripadvisor.cn/Attractions-g1017051-Activities-Jiamusi_Heilongjiang.html',
    '大庆市': 'https://www.tripadvisor.cn/Attractions-g1076271-Activities-Daqing_Heilongjiang.html',
    '伊春市': 'https://www.tripadvisor.cn/Attractions-g1152399-Activities-Yichun_Heilongjiang.html',
    '七台河市': '',
    '鹤岗市': 'https://www.tripadvisor.cn/Attractions-g1017050-Activities-Hegang_Heilongjiang.html',
    '双鸭山市': 'https://www.tripadvisor.cn/Attractions-g1017052-Activities-Shuangyashan_Heilongjiang.html',
    '黑河市': 'https://www.tripadvisor.cn/Attractions-g1017049-Activities-Heihe_Heilongjiang.html',
    '绥芬河市': 'https://www.tripadvisor.cn/Attractions-g1152403-Activities-Suifenhe_Heilongjiang.html',
    '绥化市': '',
    '大兴安岭地区': '',
    '无锡市': 'https://www.tripadvisor.cn/Attractions-g297443-Activities-Wuxi_Jiangsu.html',
    '徐州市': 'https://www.tripadvisor.cn/Attractions-g658437-Activities-Xuzhou_Jiangsu.html',
    '常州市': 'https://www.tripadvisor.cn/Attractions-g656832-Activities-Changzhou_Jiangsu.html',
    '苏州市': 'https://www.tripadvisor.cn/Attractions-g297442-Activities-Suzhou_Jiangsu.html',
    '南通市': 'https://www.tripadvisor.cn/Attractions-g641711-Activities-Nantong_Jiangsu.html',
    '连云港市': 'https://www.tripadvisor.cn/Attractions-g658456-Activities-Lianyungang_Jiangsu.html',
    '淮安市': 'https://www.tripadvisor.cn/Attractions-g1017015-Activities-Huai_an_Jiangsu.html',
    '盐城市': 'https://www.tripadvisor.cn/Attractions-g676082-Activities-Yancheng_Jiangsu.html',
    '扬州市': 'https://www.tripadvisor.cn/Attractions-g494934-Activities-Yangzhou_Jiangsu.html',
    '镇江市': 'https://www.tripadvisor.cn/Attractions-g297444-Activities-Zhenjiang_Jiangsu.html',
    '泰州市': 'https://www.tripadvisor.cn/Attractions-g641712-Activities-Taizhou_Jiangsu.html',
    '宿迁市': 'https://www.tripadvisor.cn/Attractions-g1017014-Activities-Suqian_Jiangsu.html',
    '宁波市': 'https://www.tripadvisor.cn/Attractions-g297470-Activities-Ningbo_Zhejiang.html',
    '温州市': 'https://www.tripadvisor.cn/Attractions-g297472-Activities-Wenzhou_Zhejiang.html',
    '嘉兴市': 'https://www.tripadvisor.cn/Attractions-g790186-Activities-Jiaxing_Zhejiang.html',
    '湖州市': 'https://www.tripadvisor.cn/Attractions-g659301-Activities-Huzhou_Zhejiang.html',
    '绍兴市': 'https://www.tripadvisor.cn/Attractions-g297471-Activities-Shaoxing_Zhejiang.html',
    '台州市': 'https://www.tripadvisor.cn/Attractions-g635523-Activities-Taizhou_Zhejiang.html',
    '金华市': 'https://www.tripadvisor.cn/Attractions-g608468-Activities-Jinhua_Zhejiang.html',
    '丽水市': 'https://www.tripadvisor.cn/Attractions-g677483-Activities-Lishui_Zhejiang.html',
    '芜湖市': '',
    '蚌埠市': 'https://www.tripadvisor.cn/Attractions-g1017028-Activities-Bengbu_Anhui.html',
    '淮南市': 'https://www.tripadvisor.cn/Attractions-g635517-Activities-Huainan_Anhui.html',
    '马鞍山市': 'https://www.tripadvisor.cn/Attractions-g1017030-Activities-Ma_anshan_Anhui.html',
    '安庆市': 'https://www.tripadvisor.cn/Attractions-g1017032-Activities-Anqing_Anhui.html',
    '黄山市': 'https://www.tripadvisor.cn/Attractions-g303685-Activities-Huangshan_Anhui.html',
    '滁州市': '',
    '阜阳市': '',
    '宿州市': '',
    '六安市': 'https://www.tripadvisor.cn/Attractions-g1017033-Activities-Lu_an_Anhui.html',
    '宣城市': '',
    '莆田市': 'https://www.tripadvisor.cn/Attractions-g1017023-Activities-Putian_Fujian.html',
    '三明市': 'https://www.tripadvisor.cn/Attractions-g1017022-Activities-Sanming_Fujian.html',
    '泉州市': 'https://www.tripadvisor.cn/Attractions-g303693-Activities-Quanzhou_Fujian.html',
    '漳州市': 'https://www.tripadvisor.cn/Attractions-g608460-Activities-Zhangzhou_Fujian.html',
    '南平市': 'https://www.tripadvisor.cn/Attractions-g494926-Activities-Nanping_Fujian.html',
    '龙岩市': 'https://www.tripadvisor.cn/Attractions-g1017024-Activities-Longyan_Fujian.html',
    '宁德市': 'https://www.tripadvisor.cn/Attractions-g1017025-Activities-Ningde_Fujian.html',
    '景德镇市': 'https://www.tripadvisor.cn/Attractions-g303749-Activities-Jingdezhen_Jiangxi.html',
    '萍乡市': '',
    '九江市': 'https://www.tripadvisor.cn/Attractions-g494935-Activities-Jiujiang_Jiangxi.html',
    '新余市': 'https://www.tripadvisor.cn/Attractions-g1016924-Activities-Xinyu_Jiangxi.html',
    '鹰潭市': 'https://www.tripadvisor.cn/Attractions-g1016923-Activities-Yingtan_Jiangxi.html',
    '赣州市': 'https://www.tripadvisor.cn/Attractions-g1016926-Activities-Ganzhou_Jiangxi.html',
    '吉安市': '',
    '宜春市': 'https://www.tripadvisor.cn/Attractions-g644036-Activities-Yichun_Jiangxi.html',
    '上饶市': 'https://www.tripadvisor.cn/Attractions-g1016927-Activities-Shangrao_Jiangxi.html',
    '淄博市': 'https://www.tripadvisor.cn/Attractions-g679674-Activities-Zibo_Shandong.html',
    '枣庄市': 'https://www.tripadvisor.cn/Attractions-g1017008-Activities-Zaozhuang_Shandong.html',
    '济宁市': '',
    '泰安市': 'https://www.tripadvisor.cn/Attractions-g303761-Activities-Tai_an_Shandong.html',
    '威海市': 'https://www.tripadvisor.cn/Attractions-g297459-Activities-Weihai_Shandong.html',
    '日照市': 'https://www.tripadvisor.cn/Attractions-g659917-Activities-Rizhao_Shandong.html',
    '莱芜市': '',
    '德州市': '',
    '聊城市': 'https://www.tripadvisor.cn/Attractions-g1017005-Activities-Liaocheng_Shandong.html',
    '滨州市': '',
    '菏泽市': '',
    '开封市': 'https://www.tripadvisor.cn/Attractions-g494930-Activities-Kaifeng_Henan.html',
    '洛阳市': 'https://www.tripadvisor.cn/Attractions-g303731-Activities-Luoyang_Henan.html',
    '平顶山市': '',
    '安阳市': 'https://www.tripadvisor.cn/Attractions-g1016919-Activities-Pingdingshan_Henan.html',
    '鹤壁市': '',
    '新乡市': '',
    '焦作市': '',
    '新郑市': 'https://www.tripadvisor.cn/Attractions-g1152495-Activities-Xinzheng_Henan.html',
    '许昌市': 'https://www.tripadvisor.cn/Attractions-g1016917-Activities-Xuchang_Henan.html',
    '漯河市': '',
    '南阳市': 'https://www.tripadvisor.cn/Attractions-g616022-Activities-Nanyang_Henan.html',
    '信阳市': '',
    '周口市': '',
    '驻马店市': '',
    '黄石市': '',
    '十堰市': 'https://www.tripadvisor.cn/Attractions-g1017059-Activities-Shiyan_Hubei.html',
    '宜昌市': 'https://www.tripadvisor.cn/Attractions-g297438-Activities-Yichang_Hubei.html',
    '襄阳市': 'https://www.tripadvisor.cn/Attractions-g494931-Activities-Xiangyang_Hubei.html',
    '鄂州市': '',
    '荆门市': 'https://www.tripadvisor.cn/Attractions-g659298-Activities-Jingmen_Hubei.html',
    '黄冈市': 'https://www.tripadvisor.cn/Attractions-g1017061-Activities-Huanggang_Hubei.html',
    '孝感市': '',
    '随州市': '',
    '恩施土家族苗族自治州': '',
    '潜江市': '',
    '天门市': '',
    '神农架林区': 'https://www.tripadvisor.cn/Attractions-g1580992-Activities-Shennongjia_Hubei.html',
    '株洲市': 'https://www.tripadvisor.cn/Attractions-g1016985-Activities-Zhuzhou_Hunan.html',
    '湘潭市': 'https://www.tripadvisor.cn/Attractions-g1016986-Activities-Xiangtan_Hunan.html',
    '衡阳市': 'https://www.tripadvisor.cn/Attractions-g679670-Activities-Hengyang_Hunan.html',
    '邵阳市': '',
    '岳阳市': '',
    '常德市': 'https://www.tripadvisor.cn/Attractions-g1016983-Activities-Changde_Hunan.html',
    '张家界市': 'https://www.tripadvisor.cn/Attractions-g494933-Activities-Zhangjiajie_Hunan.html',
    '益阳市': 'https://www.tripadvisor.cn/Attractions-g1016984-Activities-Yiyang_Hunan.html',
    '郴州市': 'https://www.tripadvisor.cn/Attractions-g677482-Activities-Chenzhou_Hunan.html',
    '湘西土家族苗族自治州': 'https://www.tripadvisor.cn/Attractions-g660726-Activities-Fenghuang_County_Xiangxi_Tujia_and_Miao_Autonomous_Prefecture_Hunan.html',
    '珠海市': 'https://www.tripadvisor.cn/Attractions-g297418-Activities-Zhuhai_Guangdong.html',
    '汕头市': 'https://www.tripadvisor.cn/Attractions-g297414-Activities-Shantou_Guangdong.html',
    '韶关市': 'https://www.tripadvisor.cn/Attractions-g677480-Activities-Shaoguan_Guangdong.html',
    '佛山市': 'https://www.tripadvisor.cn/Attractions-g494927-Activities-Foshan_Guangdong.html',
    '深圳市': 'https://www.tripadvisor.cn/Attractions-g297415-Activities-Shenzhen_Guangdong.html',
    '江门市': 'https://www.tripadvisor.cn/Attractions-g494928-Activities-Jiangmen_Guangdong.html',
    '湛江市': 'https://www.tripadvisor.cn/Attractions-g666406-Activities-Zhanjiang_Guangdong.html',
    '茂名市': 'https://www.tripadvisor.cn/Attractions-g1017046-Activities-Maoming_Guangdong.html',
    '肇庆市': 'https://www.tripadvisor.cn/Attractions-g303703-Activities-Zhaoqing_Guangdong.html',
    '惠州市': 'https://www.tripadvisor.cn/Attractions-g297413-Activities-Huizhou_Guangdong.html',
    '梅州市': 'https://www.tripadvisor.cn/Attractions-g635520-Activities-Meizhou_Guangdong.html',
    '东莞市': 'https://www.tripadvisor.cn/Attractions-g297412-Activities-Dongguan_Guangdong.html',
    '中山市': 'https://www.tripadvisor.cn/Attractions-g297417-Activities-Zhongshan_Guangdong.html',
    '潮州市': 'https://www.tripadvisor.cn/Attractions-g303698-Activities-Chaozhou_Guangdong.html',
    '揭阳市': 'https://www.tripadvisor.cn/Attractions-g1017045-Activities-Jieyang_Guangdong.html',
    '云浮市': 'https://www.tripadvisor.cn/Attractions-g1017048-Activities-Yunfu_Guangdong.html',
    '柳州市': 'https://www.tripadvisor.cn/Attractions-g303709-Activities-Liuzhou_Guangxi.html',
    '桂林市': 'https://www.tripadvisor.cn/Attractions-g298556-Activities-Guilin_Guangxi.html',
    '梧州市': 'https://www.tripadvisor.cn/Attractions-g798010-Activities-Wuzhou_Guangxi.html',
    '北海市': 'https://www.tripadvisor.cn/Attractions-g297420-Activities-Beihai_Guangxi.html',
    '防城港市': 'https://www.tripadvisor.cn/Attractions-g1016897-Activities-Fangchenggang_Guangxi.html',
    '钦州市': 'https://www.tripadvisor.cn/Attractions-g1016903-Activities-Qinzhou_Guangxi.html',
    '贵港市': '',
    '玉林市': 'https://www.tripadvisor.cn/Attractions-g777258-Activities-Yulin_Guangxi.html',
    '百色市': '',
    '河池市': 'https://www.tripadvisor.cn/Attractions-g1016910-Activities-Hechi_Guangxi.html',
    '来宾市': 'https://www.tripadvisor.cn/Attractions-g1016911-Activities-Laibin_Guangxi.html',
    '崇左市': 'https://www.tripadvisor.cn/Attractions-g1016912-Activities-Chongzuo_Guangxi.html',
    '三亚市': 'https://www.tripadvisor.cn/Attractions-g297427-Activities-Sanya_Hainan.html',
    '三沙市': '',
    '儋州市': '',
    '琼海市': 'https://www.tripadvisor.cn/Attractions-g297428-Activities-Qionghai_Hainan.html',
    '万宁市': 'https://www.tripadvisor.cn/Attractions-g616021-Activities-Wanning_Hainan.html',
    '五指山市': 'https://www.tripadvisor.cn/Attractions-g1017017-Activities-Wuzhishan_Hainan.html',
    '东方市': 'https://www.tripadvisor.cn/Attractions-g1017018-Activities-Dongfang_Hainan.html',
    '文昌市': 'https://www.tripadvisor.cn/Attractions-g1017016-Activities-Wenchang_Hainan.html',
    '白沙黎族自治县': 'https://www.tripadvisor.cn/Attractions-g1652136-Activities-Baisha_County_Hainan.html',
    '自贡市': 'https://www.tripadvisor.cn/Attractions-g658403-Activities-Zigong_Sichuan.html',
    '攀枝花市': '',
    '泸州市': 'https://www.tripadvisor.cn/Attractions-g616025-Activities-Luzhou_Sichuan.html',
    '德阳市': '',
    '绵阳市': 'https://www.tripadvisor.cn/Attractions-g608466-Activities-Mianyang_Sichuan.html',
    '广元市': 'https://www.tripadvisor.cn/Attractions-g1016973-Activities-Guangyuan_Sichuan.html',
    '遂宁市': 'https://www.tripadvisor.cn/Attractions-g1016975-Activities-Suining_Sichuan.html',
    '内江市': '',
    '乐山市': 'https://www.tripadvisor.cn/Attractions-g303771-Activities-Leshan_Sichuan.html',
    '南充市': '',
    '雅安市': 'https://www.tripadvisor.cn/Attractions-g1016982-Activities-Ya_an_Sichuan.html',
    '巴中市': '',
    '资阳市': 'https://www.tripadvisor.cn/Attractions-g1016980-Activities-Ziyang_Sichuan.html',
    '宜宾市': 'https://www.tripadvisor.cn/Attractions-g679673-Activities-Yibin_Sichuan.html',
    '六盘水市': '',
    '遵义市': 'https://www.tripadvisor.cn/Attractions-g608461-Activities-Zunyi_Guizhou.html',
    '安顺市': 'https://www.tripadvisor.cn/Attractions-g297422-Activities-Anshun_Guizhou.html',
    '铜仁市': 'https://www.tripadvisor.cn/Attractions-g1152596-Activities-Tongren_Guizhou.html',
    '毕节市': 'https://www.tripadvisor.cn/Attractions-g1152598-Activities-Bijie_Guizhou.html',
    '黔西南布依族苗族自治州': '',
    '黔东南苗族侗族自治州': 'https://www.tripadvisor.cn/Attractions-g21012901-Activities-Qiandongnan_Miao_and_Dong_Autonomous_Prefecture_Guizhou.html',
    '黔南布依族苗族自治州': 'https://www.tripadvisor.cn/Attractions-g21067604-Activities-Qiannan_Buyei_and_Miao_Autonomous_Prefecture_Guizhou.html',
    '曲靖市': '',
    '玉溪市': '',
    '保山市': '',
    '昭通市': '',
    '丽江市': 'https://www.tripadvisor.cn/Attractions-g303783-Activities-Lijiang_Yunnan.html',
    '普洱市': 'https://www.tripadvisor.cn/Attractions-g946447-Activities-Pu_er_Yunnan.html',
    '德宏傣族景颇族自治州': '',
    '大理白族自治州': '',
    '楚雄彝族自治州': '',
    '怒江傈僳族自治州': 'https://www.tripadvisor.cn/Attractions-g1795655-Activities-Gongshan_County_Nujiang_Lisu_Autonomous_Prefecture_Yunnan.html',
    '临沧市': '',
    '西双版纳傣族自治州': 'https://www.tripadvisor.cn/Attractions-g528741-Activities-Jinghong_Xishuangbanna_Dai_Autonomous_Prefecture_Yunnan.html',
    '日喀则市': 'https://www.tripadvisor.cn/Attractions-g303776-Activities-Shigatse_Tibet.html',
    '那曲市': '',
    '林芝市': 'https://www.tripadvisor.cn/Attractions-g734638-Activities-Nyingchi_County_Tibet.html',
    '昌都市': '',
    '石嘴山市': '',
    '吴忠市': 'https://www.tripadvisor.cn/Attractions-g1016930-Activities-Wuzhong_Ningxia.html',
    '嘉峪关市': 'https://www.tripadvisor.cn/Attractions-g303696-Activities-Jiayuguan_Gansu.html',
    '金昌市': 'https://www.tripadvisor.cn/Attractions-g1017037-Activities-Jinchang_Gansu.html',
    '平凉市': '',
    '定西市': 'https://www.tripadvisor.cn/Attractions-g1017042-Activities-Dingxi_Gansu.html',
    '陇南市': 'https://www.tripadvisor.cn/Attractions-g1757099-Activities-Longnan_Gansu.html',
    '庆阳市': '',
    '海东市': 'https://www.tripadvisor.cn/Attractions-g7299174-Activities-Haidong_Qinghai.html',
    '海西州': '',
    '黄南藏族自治州': '',
    '果洛藏族自治州': '',
    '玉树藏族自治州': '',
    '海北藏族自治州': '',
    '海西蒙古族藏族自治州': '',
    '喀什市': 'https://www.tripadvisor.cn/Attractions-g1152622-Activities-Kashgar_Xinjiang_Uygur.html',
    '和田市': 'https://www.tripadvisor.cn/Attractions-g528737-Activities-Hotan_Xinjiang_Uygur.html',
    '哈密市': 'https://www.tripadvisor.cn/Attractions-g788146-Activities-Hami_Xinjiang_Uygur.html',
    '克拉玛依市': 'https://www.tripadvisor.cn/Attractions-g658452-Activities-Karamay_Xinjiang_Uygur.html',
    '阿克苏市': '',
    '库尔勒市': 'https://www.tripadvisor.cn/Attractions-g681069-Activities-Korla_Bayingolin_Mongol_Autonomous_Prefecture_Xinjiang_Uygur.html',
    '莎车市': 'https://www.tripadvisor.cn/Attractions-g1829260-Activities-Shache_County_Xinjiang_Uygur.html',
    '伊犁哈萨克自治州': '',
    '阿勒泰地区': '',
    '高雄市': '',
    '台中市': '',
    '台南市': '',
    '花莲市': '',
    '屏东县': '',
    '基隆市': '',
    '桃园市': '',
    '彰化市': '',
    '云林县': '',
    '嘉义市': '',
    '马祖': '',
    '金门': '',
    '澎湖': ''
}


def scrape_locations_and_comments(url):
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)

            # 查找所有位置块
            location_blocks = page.locator('.EsZYd article.bMktZ')

            # 如果没有找到位置块，抛出错误
            if location_blocks.count() == 0:
                raise ValueError("未找到位置块，请检查选择器或页面内容。")

            locations_and_comments = []

            for block in location_blocks.all():
                try:
                    # 提取位置标题
                    title_locator = block.locator('header.fFeLV h3.WlYyy')
                    title = title_locator.inner_text().strip()

                    # 提取评论数
                    comments_locator = block.locator('a.iPqaD .WlYyy.diXIH.bGusc.bQCoY')
                    comments_text = comments_locator.inner_text().strip()
                    comments_count = comments_text.split('条')[0]  # 解析评论数量

                    # 提取链接
                    link_locator = block.locator('a.iPqaD')
                    href = link_locator.get_attribute('href').strip()

                    locations_and_comments.append((title, comments_count, href))
                except Exception as e:
                    print(f"处理位置块时出错: {e}")
                    continue  # 继续处理下一个位置块

            browser.close()
            return locations_and_comments
        except Exception as e:
            print(f"发生错误: {e}")
            browser.close()
            return []


def extract_after_period(s):
    # 查找'.'的位置
    period_index = s.find('.')

    # 如果'.'存在，提取其后的内容
    if period_index != -1:
        return s[period_index + 1:].strip()
    else:
        return ''  # 如果没有找到'.'，返回空字符串


def save_to_excel(data, filename):
    # 将数据转换为 DataFrame
    df = pd.DataFrame(data, columns=['City', 'Title', 'Comment', 'Link'])
    # 将 DataFrame 保存到 Excel 文件
    df.to_excel(filename, index=False, engine='openpyxl')


if __name__ == '__main__':
    all_data = []
    for city, url in Tripadvisor_province_capitals.items():
        try:
            print(f'{city}:')
            print('位置、评论数与链接一一对应:')
            data = scrape_locations_and_comments(url)
            for title, comment, link in data:
                title = extract_after_period(title)
                link = 'https://www.tripadvisor.cn/' + link
                print(f'位置: {title}')
                print(f'评论数: {comment}')
                print(f'链接: {link}')
                all_data.append((city, title, comment, link))
            print()

        except Exception as e:
            print(f"{city} 的数据抓取过程中出现问题: {e}")
    for city, url in Tripadvisor_other_cities.items():
        try:
            print(f'{city}:')
            print('位置、评论数与链接一一对应:')
            data = scrape_locations_and_comments(url)
            for title, comment, link in data:
                title = extract_after_period(title)
                link = 'https://www.tripadvisor.cn/' + link
                print(f'位置: {title}')
                print(f'评论数: {comment}')
                print(f'链接: {link}')
                all_data.append((city, title, comment, link))
            print()

        except Exception as e:
            print(f"{city} 的数据抓取过程中出现问题: {e}")
    if not os.path.exists('./temp'):
        os.mkdir('./temp')
    save_to_excel(all_data, './temp/tripadvisor_data.xlsx')
    print('数据储存成功保存')