import re
import pandas as pd
import snownlp
from collections import defaultdict, Counter
import jieba.analyse

# 加载 Excel 文件
file_path = './temp/target/combined_comments.xlsx'
data = pd.read_excel(file_path)

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
stopwords = load_stopwords('./stopwords.txt')
print(len(stopwords))


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
        comment = re.sub(r'[^\w\s.,!?，。！？\u4e00-\u9fff]',
                         '', comment, flags=re.UNICODE)
        # 去除多余的空格
        comment = ' '.join(comment.split())
        return comment

    return ''


cnt = 0
unique_comments = set()
# 初始化用于存储城市和预处理后的评论的数据
preprocessed_comments = []
last_city = '_'
# 处理每一条评论
for index, row in data.iterrows():
    city = row['城市']
    comment = row['评论内容']

    cnt += 1
    # 清空set
    if last_city != city:
        print(f'{last_city} is ok')
        unique_comments = set()
        last_city = city
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
                s = snownlp.SnowNLP(comment)
                sentiment_score = s.sentiments

                # print(comment)
                unique_comments.add(comment)
                preprocessed_comments.append({'城市': city, '评论': comment})

                # 分类情感
                if sentiment_score > positive_threshold:
                    emotion_count[city]['积极'] += 1
                elif sentiment_score < neutral_threshold:
                    emotion_count[city]['消极'] += 1
                else:
                    emotion_count[city]['中立'] += 1

                # 提取关键词（去除停用词）
                keywords = jieba.analyse.extract_tags(
                    comment, topK=1, withWeight=False)
                # 关键词过滤
                filtered_keywords = [
                    word for word in keywords if word not in stopwords and not word.isdigit()]

                # 更新每个城市的关键词
                for word in filtered_keywords:
                    city_keywords[city][word] += 1
        except Exception as e:
            print(f"情感分析失败: {e}")
    else:
        print(f"无效的评论内容: {comment}")
        print(f"评论内容的类型: {type(comment)}")


def score_frequency(freq):
    if freq >= 40:
        return 5
    elif freq >= 20:
        return 4
    elif freq >= 10:
        return 3
    elif freq >= 5:
        return 2
    else:
        return 1
    # return freq


# 创建用于存储关键词和分数的数据
keyword_scores = []

# 计算每个城市的关键词及其频率
for city, keywords in city_keywords.items():
    for word, freq in keywords.items():
        score = score_frequency(freq)
        if freq > 3:  # 只保存出现次数大于3的关键字
            keyword_scores.append({
                '城市': city,
                '关键字': word,
                '分数': score
            })

# 创建 DataFrame
keyword_df = pd.DataFrame(keyword_scores)
# 保存到 Excel 文件
keyword_output_file = './temp/target/城市关键词评分.xlsx'
keyword_df.to_excel(keyword_output_file, index=False)
print(f"关键词评分已保存到 {keyword_output_file}")
print('')

# 输出情感分析结果
print("各城市的情感分析结果：")
for city, emotions in emotion_count.items():
    print(f"{city} -> 积极: {emotions['积极']
                           }, 中立: {emotions['中立']}, 消极: {emotions['消极']}")
# 转换结果为 DataFrame
emotion_df = pd.DataFrame.from_dict(
    emotion_count, orient='index').reset_index()
emotion_df.columns = ['城市', '积极评论', '中立评论', '消极评论']
# 保存到 Excel 文件
output_file = './temp/target/城市情感分析结果.xlsx'
emotion_df.to_excel(output_file, index=False)
print(f"情感分析结果已保存到 {output_file}")
print('')

# 创建 DataFrame 并保存预处理后的评论
preprocessed_df = pd.DataFrame(preprocessed_comments)
preprocessed_file = './temp/target/城市预处理评论.xlsx'
preprocessed_df.to_excel(preprocessed_file, index=False)
print(f"预处理后的评论已保存到 {preprocessed_file}")
