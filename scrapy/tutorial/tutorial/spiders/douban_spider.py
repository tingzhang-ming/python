from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import DoubanItem as GroupInfo


class MySpider(CrawlSpider):
    name = 'douban.xp'
    current = ''
    allowed_domains = ['douban.com']

    def __init__(self, target=None):
        if self.current is not '':
            target = self.current
        if target is not None:
            self.current = target
        self.start_urls = [
            'http://www.douban.com/group/explore?tag=%s' % (target)
        ]
        self.rules = (
            Rule(LinkExtractor(allow=('/group/explore[?]start=.*?[&]tag=.*?$',),
                               restrict_xpaths=('//span[@class="next"]')), callback='parse_next_page', follow=True),
        )
        # call the father base function
        super(MySpider, self).__init__()

    def parse_next_page(self, response):
        self.logger.info(msg='begin init the page %s ' % response.url)
        list_item = response.xpath('//a[@class="nbg"]')

        # check the group is not null
        if list_item is None:
            self.logger.info(msg='cant select anything in selector ')
            return
        for a_item in list_item:
            item = GroupInfo()
            item['group_url'] = ''.join(a_item.xpath('@href').extract())
            item['group_tag'] = self.current
            item['group_name'] = ''.join(a_item.xpath('@title').extract())
            yield item

    def parse_start_url(self, response):
        self.logger.info(msg='begin init the start page %s ' % response.url)
        list_item = response.xpath('//a[@class="nbg"]')

        # check the group is not null
        if list_item is None:
            self.logger.info(msg='cant select anything in selector ')
            return
        for a_item in list_item:
            item = GroupInfo()
            item['group_url'] = ''.join(a_item.xpath('@href').extract())
            item['group_tag'] = self.current
            item['group_name'] = ''.join(a_item.xpath('@title').extract())
            yield item

    def parse_next_page_people(self, response):
        self.logger.info('Hi, this is an the next page! %s', response.url)