# encoding: utf-8
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "aad_quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     # next_page = response.urljoin(next_page)
        #     # yield scrapy.Request(next_page, callback=self.parse)
        #     yield response.follow(next_page, callable=self.parse)
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)
