# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
from scrapy_splash import SplashMiddleware
from scrapy.http import Request, HtmlResponse
from scrapy.selector import Selector
from scrapy_splash import SplashRequest
from AAG_splash_test.items import SplashTestItem
import sys
import os
import re
import time

reload(sys)
sys.setdefaultencoding('utf-8')

sys.stdout = open('output.txt', 'w')

# 不设置user-agent，response就是空 - -

class toutiaoSpider(Spider):
    name = 'toutiao'

    base_url = 'http://www.toutiao.com/search/?keyword='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            url = self.base_url + keyword
            yield SplashRequest(url, callback=self.parse,
                                args={'wait': 2},
                                meta={'keyword': keyword})

    def date_isValid(self, strDateText):
        '''
        判断日期时间字符串是否合法：如果给定时间大于当前时间是合法，或者说当前时间给定的范围内
        :param strDateText: 四种格式 '2小时前'; '2天前' ; '昨天' ;'2017.2.12 '
        :return: True:合法；False:不合法
        '''
        currentDate = time.strftime('%Y-%m-%d')
        if strDateText.find('分钟前') > 0 or strDateText.find('刚刚') > -1:
            return True, currentDate
        elif strDateText.find('小时前') > 0:
            datePattern = re.compile(r'\d{1,2}')
            ch = int(time.strftime('%H'))  # 当前小时数
            strDate = re.findall(datePattern, strDateText)
            if len(strDate) == 1:
                if int(strDate[0]) <= ch:  # 只有小于当前小时数，才认为是今天
                    return True, currentDate
        return False, ''

    def parse(self, response):
        site = Selector(response)
        # it_list = []
        keyword = response.meta['keyword']
        sels = site.xpath('//div[@class="articleCard"]')
        for sel in sels:
            dates = sel.xpath('.//span[@class="lbtn"]/text()')
            if len(dates) > 0:
                flag, date = self.date_isValid(dates[0].extract())
                if flag:
                    url = 'http://www.toutiao.com' + str(sel.xpath('.//a[@class="link title"]/@href')[0].extract())
                    url = url[:len(url)-1]
                    source=str(sel.xpath('.//a[@class="lbtn source J_source"]/text()')[0].extract())
                    yield scrapy.Request(url, callback=self.parse_item,
                                         meta={'date': date, 'url': url,
                                               'keyword': keyword, 'source': source}
                                         )

    def parse_item(self, response):
        site = Selector(response)
        it = SplashTestItem()
        titles = site.xpath('/html/head/title/text()')
        if len(titles) > 0:
            keyword = response.meta['keyword']
            strtiltle = str(titles[0].extract())
            if strtiltle.find(keyword) > -1:
                it['title'] = strtiltle
                it['url'] = response.meta['url']
                it['date'] = response.meta['date']
                it['keyword'] = keyword
                it['source'] = response.meta['source']
                return it
