# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    area = scrapy.Field()


class CsdnblogItem(scrapy.Item):
    """存储提取信息数据结构"""

    article_name = scrapy.Field()
    article_url = scrapy.Field()


class BokeyuanlistItem(scrapy.Item):
    """存储提取信息数据结构"""

    article_time = scrapy.Field()
    article_name = scrapy.Field()
    article_url = scrapy.Field()

