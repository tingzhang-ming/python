#!/usr/bin/python
# -*- coding:utf-8 -*-

# from scrapy.contrib.spiders import  CrawlSpider,Rule
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from tutorial.items import BokeyuanlistItem


def get(l):
    if len(l) > 0:
        return l[0]
    else:
        return ""


class CSDNBlogSpider(Spider):
    """爬虫CSDNBlogSpider"""

    name = "bokeyuanlist"

    # 减慢爬取速度 为1s
    download_delay = 1
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        # "http://www.cnblogs.com/codefish"
        "http://www.cnblogs.com/mhc-fly"
    ]

    def parse(self, response):
        sel = Selector(response)
        item = BokeyuanlistItem()
        details = sel.xpath('//div[@id="mainContent"]/div/div')
        print len(details)
        for d in details:
            article_time = d.xpath('div[@class="dayTitle"]/a/text()').extract()
            article_name = d.xpath('div[@class="postTitle"]/a/text()').extract()
            article_url = d.xpath('div[@class="postCon"]/div/a/@href').extract()
            item['article_time'] = [get(article_time).encode('utf-8')]
            item['article_name'] = [get(article_name).encode('utf-8')]
            item['article_url'] = [get(article_url).encode('utf-8')]
            yield item

        # 下一页
        urls = sel.xpath('//div[@id="nav_next_page"]/a/@href').extract()
        if len(urls) > 0:
            yield Request(urls[0], callback=self.parse)
        aas = sel.xpath('//div[@id="homepage_top_pager"]/div/a')
        if len(aas) > 0:
            for aa in aas:
                if aa.xpath('./text()').extract_first() == "下一页":
                    urls = aa.xpath('./@href').extract()
                    if len(urls) > 0:
                        yield Request(urls[0], callback=self.parse)

