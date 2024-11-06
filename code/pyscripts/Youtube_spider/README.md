#### 说明： ####
    1.使用Get_videos_links.py脚本爬取Youtube中的中国城市视频链接;
    2.使用Get_comments.py脚本对视频下的评论进行爬取;
    3.爬取好评论后，使用Sentiment_analysis.py脚本对评论进行情感分析和关键字提取。
    4.运行上述三个脚本后，会得到 youtube_links_by_{city}.xlsx、youtube_comments_{city}.xlsx、省会/非省会城市关键词评分_中/英.xlsx、
    省会/非省会城市情感分析结果.xlsx文件
    特别标注：对于想获取的频道视频链接和视频下的评论，可以使用youtube的api。

#### 另一个说明 ####
``` bash
cd Youyube_spider
run.bat [venvPath]
```