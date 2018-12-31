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

class weizhongquanSpider(Spider):
    name = 'weizhongquan'


    base_url = 'http://www.toutiao.com/search/?keyword='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            url = self.base_url + keyword
            yield SplashRequest(url, callback=self.parse,
                                args={'wait': 2},
                                meta={'keyword': keyword})


    def Comapre_to_days(self,leftdate, rightdate):
        '''
        比较连个字符串日期，左边日期大于右边日期多少天
        :param leftdate: 格式：2017-04-15
        :param rightdate: 格式：2017-04-15
        :return: 天数
        '''
        l_time = time.mktime(time.strptime(leftdate, '%Y-%m-%d'))
        r_time = time.mktime(time.strptime(rightdate, '%Y-%m-%d'))
        result = int(l_time - r_time) / 86400
        return result

    def date_isValid(self, strDateText):
        '''
        判断日期时间字符串是否合法：如果给定时间大于当前时间是合法，或者说当前时间给定的范围内
        :param strDateText: 四种格式 '2小时前'; '2天前' ; '昨天' ;'2017.2.12 '
        :return: True:合法；False:不合法
        '''
        currentDate = time.strftime('%Y-%m-%d')
        datePattern = re.compile(r'\d{4}-\d{1,2}-\d{1,2}')
        strDate = re.findall(datePattern, strDateText)
        if len(strDate) == 1:
            if self.Comapre_to_days(currentDate,strDate[0])==0:
                return True,currentDate
        return False, ''
    def parse(self, response):
        site = Selector(response)
        keyword = response.meta['keyword']
        sels = site.xpath('//li[@class="itemtitle"]')
        for sel in sels:
            titles = sel.xpath('.//text()')
            title =str(titles[1].extract())
            flag,date =self.date_isValid(str(titles[2].extract()))
            if flag and title.find(keyword)>-1:
                url = 'http://www.v4.cc'+ str(sel.xpath('.//a/@href')[0].extract())
                yield SplashRequest(url
                                        , self.parse_item
                                        , args={'wait': '1'},
                                        meta={'date': date, 'url': url,
                                                  'keyword': keyword,'title':title}
                                            )


    def parse_item(self, response):
        site = Selector(response)
        it = SplashTestItem()
        it['title'] = response.meta['title']
        it['url'] = response.meta['url']
        it['date'] = response.meta['date']
        it['keyword'] = response.meta['keyword']
        sources = site.xpath('//div[@class="wxshare"]/span/a/text()')
        if len(sources)>0:
            it['source'] = sources[0].extract()
        return it
