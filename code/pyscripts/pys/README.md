### 1.使用setup.sql初始化数据库表
### 2.运行python脚本：
```bash
cd ./pyscripts/pys
# 爬取旅游相关信息
python trvl_spider.py [index] [user] [passwd] [database]
# 爬取事物相关信息
python sfd_spider.py [depth] [user] [passwd] [database]
# 爬取NewYork新闻相关信息
python NewYork.py [city_dick.json path]
```
    