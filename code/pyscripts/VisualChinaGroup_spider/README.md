#### 说明： ####
    1.使用Get_city_img_url.py脚本爬取视觉中国中的中国城市图片链接;
    2.使用Combine_city_img.py脚本对爬取到的城市图片链接进行汇总;
    3.如果有需要，可以使用 拼音转中文.py 将汇总的xlsx文件中的城市名和所属省份由拼音转成中文
#### 另一个说明 ####
``` bash
cd VisualChinaGroup_spider
run.bat -v venvPath -c "city1 city2..." 
# city1 city2使用中文即可 不用-c参数以爬取全部 默认数据库为 root 123456 ry-vue 如有需要请修改save_to_db.py
# usage run.bat -v "D:\venv\.venv" -c "天津市 北京市"
```
