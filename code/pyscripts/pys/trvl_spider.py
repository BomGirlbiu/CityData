# target site https://travel.qunar.com
import sys
import json
import logging
import pymysql
import os
from pymysql.converters import escape_string
from bs4 import BeautifulSoup
from util import utils


if not os.path.exists('./log'):
    os.makedirs('./log')
# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(
                            "./log/trvl_spider.log", encoding='utf-8'),
                        logging.StreamHandler()
                    ])

infos = []
INFOS_URL_TEMPLATE = 'https://travel.qunar.com/p-sx{}?area={}&month={}&tag={}&hot={}'
PAGE = 1
AREA = 1
MONTH = 0
THEME = 0
HOT = 0


def get_infos(url):
    soup = BeautifulSoup(utils.ask_url(url), "html.parser")
    logging.info('get_infos: %s', url)
    for item in soup.find_all('div', class_='imgbox'):
        spans = item.find('div').find_all('span')
        area = spans[0].text
        up_area = spans[1].text
        src = item.find('a').get('href')
        img = item.find('img').get('src')
        if up_area == '中国':
            up_area = area + '市'
        info = {
            'src': src,
            'img': img,
            'area': area,
            'up_area': up_area
        }
        infos.append(info)


def save_infos_to_json():
    with open('infos.json', 'a', encoding='utf-8') as f:
        json.dump(infos, f, ensure_ascii=False, indent=4)


def save_infos_to_db(user='root', passwd='123456', db='ry-vue'):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=passwd,
        charset='utf8mb4',
        database=db
    )
    cursor = conn.cursor()
    logging.info('save_infos_to_db: %d', len(infos))

    try:
        conn.begin()
        for info in infos:
            cursor.execute(
                "INSERT INTO city_travel(src, img, city, province, title, content) VALUES (%s, %s, %s, %s, %s, %s)",
                (escape_string(info['src']), escape_string(info['img']), escape_string(info['area']),
                    escape_string(info['up_area']), escape_string(info['title']), escape_string(info['content']))
            )
        conn.commit()
    except pymysql.MySQLError as e:
        logging.error("MySQL Error: %s", e)
        conn.rollback()
    except Exception as e:
        logging.error("Unexpected Error: %s", e)
        conn.rollback()


def parse_src():
    for info in infos[:]:
        url = info['src']
        logging.info('parse: %s', url)
        soup = BeautifulSoup(utils.ask_url(url), "html.parser")
        items = soup.find_all('div', class_='c_item')
        if not items:
            infos.remove(info)
            continue
        title = items[0].text
        content_index = 1 if len(items) < 3 else 2
        content = items[content_index].text.replace('\n', '').replace(
            '\r', '').replace('\t', '').replace('\u200b', '')
        info['title'] = title
        info['content'] = content


if __name__ == '__main__':
    user = 'root'
    passwd = '20020316'
    db = 'ry-vue'
    index = 2
    try:
        index = int(sys.argv[1])
        index += 1
        user = sys.argv[2]
        passwd = sys.argv[3]
        db = sys.argv[4]
    except IndexError as e:
        logging.info('missing command line arguments, using default db')
    except ValueError as e:
        logging.info('invalid index argument, using default index 2')
    for i in range(1, index):
        get_infos(INFOS_URL_TEMPLATE.format(i, AREA, MONTH, THEME, HOT))
        parse_src()
        save_infos_to_db(user, passwd, db)
        infos = []
    logging.info('done')
