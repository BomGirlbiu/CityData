#### 说明： ####
    1.使用Get_city_news_url.py脚本爬取GoogleNews中的中国城市新闻链接;
    2.使用Combine_city_news.py脚本对爬取到的中国城市新闻链接进行汇总;
    3.如果有需要，可以使用 拼音转中文.py 将汇总的xlsx文件中的城市名和所属省份由拼音转成中文
#### 另一种用法 ####
```baseh
    cd GoogleNews_spider
    # make sure you have city_dict.json in this dir
    run.bat venvPath
    # output file will be in ./temp/target
```