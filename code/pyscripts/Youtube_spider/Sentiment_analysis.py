
# 对youtube评论进行情感分析

# nltk（自然语言工具包，用于处理语言数据）
# SnowNLP（用于中文情感分析和其他中文处理）
# jieba（中文分词工具）
# langdetect（语言检测工具）

import re
import pandas as pd
from nltk.corpus import stopwords
from snownlp import SnowNLP
from collections import defaultdict, Counter
import jieba
import jieba.analyse
import os
from langdetect import detect, DetectorFactory
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# 解决 langdetect 的随机性问题
DetectorFactory.seed = 0

# 初始化 NLTK 的情感分析工具
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

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

# 初始化用于存储城市和预处理后的评论的数据
preprocessed_comments = []

# 初始化存储情感分类结果和关键词的字典
emotion_count = defaultdict(lambda: {'积极': 0, '中立': 0, '消极': 0})
city_keywords = defaultdict(Counter)

# 定义情感分类阈值
positive_threshold = 0.7
neutral_threshold = 0.4


# 假设 stopwords.txt 文件每行一个停用词
def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(line.strip() for line in file)


# 加载停用词
stopwords2 = load_stopwords('stopwords2.txt')
print(len(stopwords2))


# 下载 NLTK 的停用词列表（如果未下载）
nltk.download('stopwords')
# 停用词
stop_words = set(stopwords.words('english'))


def extract_keywords_tfidf(text, top_n=2):
    """
    使用 TF-IDF 提取关键词
    参数:
    - text: str，待提取关键词的文本
    - top_n: int，提取的关键词数量
    返回:
    - keywords: list，提取的关键词列表
    """
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 1))  # 使用内置英文停用词
    X = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    scores = X.toarray().flatten()
    word_scores = list(zip(feature_names, scores))
    sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)
    keywords = [word for word, score in sorted_words[:top_n]]
    return keywords


# 对评论文本进行预处理
def preprocess_comment(comment):
    """
    对评论文本进行预处理，包括去除 HTML 标签、网址、特殊字符、表情符号，
    以及去除多余空格。
    参数:
    - comment: str，待处理的评论文本
    返回:
    - 处理后的评论文本
    """
    if isinstance(comment, str):
        # 去除 HTML 标签
        comment = re.sub(r'<[^>]+>', '', comment)
        # 去除网址和链接
        comment = re.sub(r'http\S+', '', comment)
        # 去除表情符号和Emoji（范围包括所有 Unicode 表情符号）
        comment = re.sub(r'[^\w\s.,!?，。！？\u4e00-\u9fff]', '', comment, flags=re.UNICODE)
        # 去除多余的空格
        comment = ' '.join(comment.split())
        return comment
    return ''


def score_frequency(freq):
    if freq >= 50:
        return 5
    elif freq >= 30:
        return 4
    elif freq >= 20:
        return 3
    elif freq >= 10:
        return 2
    else:
        return 1


def analyze_sentiment(text):
    """
    根据评论的语言类型选择不同的情感分析工具。
    参数:
    - text: str，评论文本
    返回:
    - dict，包含情感得分和类型的结果
    """
    try:
        # 检测语言
        lang = detect(text)

        if lang == 'zh-cn' or lang == 'zh-tw':
            # 中文评论，使用 SnowNLP
            s = SnowNLP(text)
            sentiment_score = s.sentiments  # SnowNLP 返回的是情感得分，范围在0到1之间
            sentiment_type = '积极' if sentiment_score > positive_threshold else '消极' if sentiment_score < neutral_threshold else '中立'
        elif lang == 'en':
            # 英文评论，使用 NLTK
            sentiment_score = sia.polarity_scores(text)['compound']
            sentiment_type = '积极' if sentiment_score > positive_threshold else '消极' if sentiment_score < -positive_threshold else '中立'
        else:
            sentiment_score = None
            sentiment_type = '未知语言'

        return {
            '情感得分': sentiment_score,
            '情感类型': sentiment_type
        }
    except Exception as e:
        return {
            '情感得分': None,
            '情感类型': f'分析失败: {e}'
        }


def sentiment_analysis(city_name):
    file_path = f'./temp/youtube_comments_{city_name}.xlsx'
    data = pd.read_excel(file_path)
    unique_comments = set()
    cnt1 = 0
    cnt2 = 0
    # 处理每一条评论
    for index, row in data.iterrows():
        city = city_name
        comment = row['comment']

        if isinstance(comment, str):
            try:
                # 找到 ':' 的位置
                colon_index = comment.find(':')
                reply_index = comment.find("回复")
                # 如果找到了 ':'
                if colon_index != -1 and reply_index != -1:
                    # 提取 ':' 后面的部分
                    comment = comment[colon_index + 1:].strip()

                # 预处理评论
                comment = preprocess_comment(comment)
                # 评论去重
                if comment not in unique_comments:
                    # 情感分析
                    sentiment_result = analyze_sentiment(comment)
                    sentiment_type = sentiment_result['情感类型']

                    if sentiment_type == '积极':
                        emotion_count[city]['积极'] += 1
                    elif sentiment_type == '消极':
                        emotion_count[city]['消极'] += 1
                    elif sentiment_type == '中立':
                        emotion_count[city]['中立'] += 1

                    unique_comments.add(comment)
                    preprocessed_comments.append({'城市': city, '评论': comment})

                    # 检测语言
                    lang = detect(comment)
                    if lang == 'zh-cn' or lang == 'zh-tw':
                        # 提取关键词（去除停用词）
                        keywords = jieba.analyse.extract_tags(comment, topK=1, withWeight=False)
                        # 关键词过滤
                        filtered_keywords = [word for word in keywords if word not in stopwords2 and not word.isdigit()]
                        # 更新每个城市的关键词
                        for word in filtered_keywords:
                            city_keywords[city][word] += 1
                        cnt1 += 1
                    elif lang == 'en':
                        # 提取英文关键词
                        filtered_keywords = extract_keywords_tfidf(comment, top_n=2)
                        # 更新每个城市的关键词
                        for word in filtered_keywords:
                            city_keywords[city][word] += 1
                        cnt2 += 1
                    else:
                        filtered_keywords = []

            except Exception as e:
                cnt = 1
                # print(f"情感分析失败: {e}")
        else:
            print(f"无效的评论内容: {comment}")
            print(f"评论内容的类型: {type(comment)}")
    print(f'{city_name}: {cnt1} {cnt2}')


# 遍历城市
# for city_pinyin, city_name in province_capitals.items():
#     excel_file = f'./youtube_comments_{city_name}.xlsx'
#     if os.path.exists(excel_file):
#         print(f"处理城市: {city_name} ({city_pinyin})")
#         sentiment_analysis(city_name)
#     else:
#         print(f"{excel_file} 文件不存在.")

for city_pinyin, city_name in other_cities.items():
    excel_file = f'./temp/youtube_comments_{city_name}.xlsx'
    if os.path.exists(excel_file):
        print(f"处理城市: {city_name} ({city_pinyin})")
        sentiment_analysis(city_name)
    else:
        print(f"{excel_file} 文件不存在.")

# 创建用于存储关键词和分数的数据
keyword_scores_Chinese = []
keyword_scores_English = []

# 计算每个城市的关键词及其频率
for city, keywords in city_keywords.items():
    for word, freq in keywords.items():
        score = score_frequency(freq)
        if freq > 5:  # 只保存出现次数大于5的关键字
            if word not in stopwords2:
                print(f'{word} {freq}')
                if any(char.islower() for char in word) or any(char.isupper() for char in word):
                    keyword_scores_English.append({
                        '城市': city,
                        '关键字': word,
                        '分数': score
                    })
                else:
                    keyword_scores_Chinese.append({
                        '城市': city,
                        '关键字': word,
                        '分数': score
                    })

if not os.path.exists('./temp/target'):
    os.makedirs('./temp/target')

# 创建 DataFrame
keyword_df = pd.DataFrame(keyword_scores_Chinese)
# 保存到 Excel 文件
keyword_output_file = './temp/target/非省会城市关键词评分_中.xlsx'
keyword_df.to_excel(keyword_output_file, index=False)
print(f"关键词评分已保存到 {keyword_output_file}")
print('')

# 创建 DataFrame
keyword_df = pd.DataFrame(keyword_scores_English)
# 保存到 Excel 文件
keyword_output_file = './temp/target/非省会城市关键词评分_英.xlsx'
keyword_df.to_excel(keyword_output_file, index=False)
print(f"关键词评分已保存到 {keyword_output_file}")
print('')

# 输出情感分析结果
print("各城市的情感分析结果：")
for city, emotions in emotion_count.items():
    print(f"{city} -> 积极: {emotions['积极']}, 中立: {emotions['中立']}, 消极: {emotions['消极']}")
# 转换结果为 DataFrame
# print(emotion_count)
emotion_df = pd.DataFrame.from_dict(emotion_count, orient='index').reset_index()
# print(emotion_df)
emotion_df.columns = ['城市', '积极评论', '中立评论', '消极评论']
# 保存到 Excel 文件
output_file = './temp/target/非省会城市情感分析结果.xlsx'
emotion_df.to_excel(output_file, index=False)
print(f"情感分析结果已保存到 {output_file}")
print('')
