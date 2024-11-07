# target site https://travel.qunar.com
import sys
import logging
import pymysql
from pymysql.converters import escape_string
from util import utils
from bs4 import BeautifulSoup
import os
if not os.path.exists('./log'):
    os.makedirs('./log')

max_page_depth = 5


# 配置日志
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("./log/sfd_spider.log", encoding='utf-8'),
                              logging.StreamHandler()])

logger = logging.getLogger(__name__)


def get_infos(url):
    bs = BeautifulSoup(utils.ask_url(url), "html.parser")
    logger.info('get_infos: %s', url)
    local_infos = []
    for item in bs.find_all('dl'):
        # print(item)
        link = item.find('a')
        target = link.get('href')
        province = link.text
        logger.debug('Province: %s, Target: %s', province, target)
        local_infos.append(
            {'province': province, 'target': target, 'foodList': []})
    return local_infos


def parse_infos(local_infos):
    url = 'https://www.xiangha.com/getNativeList'
    for info in local_infos:
        pinyin = utils.get_last_word_of_url(info['target'])
        channel = 'xiaochi'
        for i in range(0, max_page_depth):
            logger.info('parse info: %s, %s, %d', pinyin, channel, i)
            data = {
                "pinyin": pinyin,
                "channel": channel,
                "page": i
            }
            h = utils.ask_url_post_as_dict(url, data)
            if h['data'] == []:
                break
            for item in h['data']:
                info['foodList'].append({
                    'name': item['name'],
                    'img': item['imgShow'],
                    'src': 'https://www.xiangha.com/techan/{}.html'.format(item['code']),
                    'summary': item['NativeInfo_summary'],
                })
    return local_infos


def save_infos_to_db(infos, user='root', passwd='123456', db='ry-vue'):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=passwd,
        charset='utf8mb4',
        database=db
    )
    cursor = conn.cursor()
    logger.info('save_infos_to_db: %d', len(infos))
    for info in infos:
        try:
            conn.begin()
            for food in info['foodList']:
                cursor.execute("insert into city_food(province, name, img, src, summary) values(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')" % (escape_string(
                    info['province']), escape_string(food['name']), escape_string(food['img']), escape_string(food['src']), escape_string(food['summary'])))
            conn.commit()
        except pymysql.MySQLError as e:
            logger.error(e)
            conn.rollback()
            continue


if __name__ == '__main__':
    user = 'root'
    passwd = '20020316'
    db = 'ry-vue'
    try:
        max_page_depth = int(sys.argv[1])
        user = sys.argv[2]
        passwd = sys.argv[3]
        db = sys.argv[4]
    except (IndexError, ValueError) as e:
        logger.info('use default db')

    infos = get_infos('https://www.xiangha.com/xiaochi/')
    infos = parse_infos(infos)
    save_infos_to_db(infos, user, passwd, db)
    logger.info('done')
