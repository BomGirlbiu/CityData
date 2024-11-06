#### 说明： ####
    1.使用Get_videos_links.py脚本爬取Bilibili中的中国城市视频链接;
    2.使用Get_comments.py脚本对视频下的评论进行爬取;
    3.爬取好评论后，使用Sentiment_analysis.py脚本对评论进行情感分析和关键字提取。
    4.运行上述三个脚本后，会得到 videos_url.xlsx、城市关键词评分.xlsx、城市预处理评论.xlsx和城市预处理评论.xlsx四个文件

#### 另一个用法： ####
    1.cd Bilibili_spider
    2.run.bat [.venvpath] [1 2...]
     [1 2...] list define which step to skip
    makesure there is a province_city_dict.json file in path

    # set scripts[1]=Get_videos_links.py ./province_city_dict.json
    # set scripts[2]=combind.py
    # set scripts[3]=Get_comments.py
    # set scripts[4]=combind.py 1
    # set scripts[5]=Sentiment_analysis.py
    # set scripts[6]=save_comments.py
    # you can also edit run.bat
