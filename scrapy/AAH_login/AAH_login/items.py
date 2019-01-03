# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class AahLoginItem(scrapy.Item):
    pass


class DoubamovieItem(scrapy.Item):
    title = scrapy.Field()  # 电影名字
    movieInfo = scrapy.Field()  # 电影的描述信息，包括导演、主演、电影类型等等
    star = scrapy.Field()  # 电影评分
    quote = scrapy.Field()  # 电影中最经典或者说脍炙人口的一句话


class ZhihuItem(scrapy.Item):
    url = Field()  # 保存抓取问题的url
    title = Field()  # 抓取问题的标题
    description = Field()  # 抓取问题的描述
    answer = Field()  # 抓取问题的答案
    name = Field()  # 个人用户的名称
