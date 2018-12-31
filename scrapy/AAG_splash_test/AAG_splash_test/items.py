# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AagJingdongMobileItem(scrapy.Item):
    # 单价
    price = scrapy.Field()
    # description = Field()
    # 促销
    promotion = scrapy.Field()
    # 增值业务
    value_add = scrapy.Field()
    # 重量
    quality = scrapy.Field()
    # 选择颜色
    color = scrapy.Field()
    # 选择版本
    version = scrapy.Field()
    # 购买方式
    buy_style = scrapy.Field()
    # 套装
    suit = scrapy.Field()
    # 增值保障
    value_add_protection = scrapy.Field()
    # 白天分期
    staging = scrapy.Field()
    # post_view_count = scrapy.Field()
    # post_comment_count = scrapy.Field()
    # url = scrapy.Field()


class SplashTestItem(scrapy.Item):
    #标题
    title = scrapy.Field()
    #日期
    date = scrapy.Field()
    #链接
    url = scrapy.Field()
    #关键字
    keyword  = scrapy.Field()
    #来源网站
    source =  scrapy.Field()


