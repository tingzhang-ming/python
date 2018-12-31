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


class toutiaoSpider(Spider):
    name = 'toutiao2'

    # start_urls = ['http://www.toutiao.com']
    start_urls = ['https://www.toutiao.com/group/6640773578314744327']

    # def parse(self, response):
    #     url = 'https://www.toutiao.com/group/6640773578314744327'
    #     yield scrapy.Request(url, callback=self.parse_item)

    def parse(self, response):
        site = Selector(response)
        it = SplashTestItem()
        tirtle2s = site.xpath('.')
        print(response)
        print(tirtle2s)
        titles = site.xpath('/html/head/title/text()')
        if len(titles) > 0:
            strtiltle = str(titles[0].extract())
            it['title'] = strtiltle
            it['url'] = "url"
            it['date'] = "date"
            it['keyword'] = "keyword"
            it['source'] = "source"
            return it
        else:
            print("kong")