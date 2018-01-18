# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup


def get_info(url):
    """获得网页内容"""
    r = requests.get(url)
    return r.content


def strip_str(s):
    return ''.join([v.strip() for v in s.split('\n')])


def parse_str(content):
    """解析结果为需要的内容"""
    soup = BeautifulSoup(content, 'lxml')
    main_info = soup.find('ul', attrs={'id': 'house-lst'})
    r = []
    for info in main_info.find_all('div', attrs={'class': 'info-panel'}):
        name = info.find('a', attrs={'target': '_blank'}).text
        price = info.find('div', attrs={'class': 'price'}).find('span').text
        square = info.find('div', attrs={'class': 'square'}).find('span').text
        place = info.find('div', attrs={'class': 'where'}).text
        r.append('\t'.join([strip_str(name),
                            strip_str(price),
                            strip_str(square),
                            strip_str(place)]))
        print name
    return '\n'.join(r)


def load_rlt(rlt, filename, columns=None):
    """将结果保存到文件里"""
    with open(filename, 'w') as fw:
        if columns:
            fw.write('\t'.join(columns) + '\n')
        fw.write(rlt)


def main(x):
    url = x
    r = get_info(url)
    rlt = parse_str(r)
    load_rlt(rlt, 'lianjia.csv')


if __name__ == '__main__':
    web = 'https://bj.lianjia.com/zufang/'
    main(web)
