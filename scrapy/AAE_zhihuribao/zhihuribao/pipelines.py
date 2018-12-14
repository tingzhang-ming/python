# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from os.path import join
import uuid
import pdfkit


class ZhihuribaoPipeline(object):

    def process_item(self, item, spider):
        url = item["url"]
        title = item['title']
        target_dir = 'D:/zhihu'
        tmp_file = str(uuid.uuid4())+'.pdf'
        tmp_path = join(target_dir, tmp_file)
        try:
            pdfkit.from_url(item["url"], tmp_path)
        except Exception as e:
            print "some error: {}".format(e.message)
        os.rename(tmp_path, join(target_dir, title.decode('utf-8')+'.pdf'))
        return item


