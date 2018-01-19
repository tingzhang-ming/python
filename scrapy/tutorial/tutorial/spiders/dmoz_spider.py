import scrapy
from tutorial.items import DmozItem


def get(l):
    if len(l) > 0:
        return l[0]
    else:
        return ''


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    # allowed_domains = ["amazon.com"]
    start_urls = [
        "http://example.webscraping.com/places/default/view/Afghanistan-1",
    ]

    def parse(self, response):
        item = DmozItem()
        item['area'] = get(response.xpath('//td[@class="w2p_fw"]').re('[\d|,]+(?= square kilometres)'))
        yield item

