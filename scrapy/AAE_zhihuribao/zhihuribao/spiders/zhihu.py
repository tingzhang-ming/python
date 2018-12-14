# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from zhihuribao.items import ZhihuribaoItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['daily.zhihu.com']
    start_urls = ['http://daily.zhihu.com/']

    def parse(self, response):
        for col in range(1, 4):
            for row in range(1, 11):
                item = ZhihuribaoItem()
                xpath_selector = "//div[@class='col-lg-4'][{0}]//div[@class='wrap'][{1}]".format(col, row)
                sub_url = response.xpath(xpath_selector + "//@href").extract_first()
                fix_url = "http://daily.zhihu.com"
                item["url"] = fix_url + sub_url
                title = response.xpath(xpath_selector + "//span/text()").extract_first()
                item["title"] = title
                yield item
