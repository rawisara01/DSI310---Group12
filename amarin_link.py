from gc import callbacks
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# https://www.amarintv.com/tags/%E0%B8%AD%E0%B8%B8%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%AB%E0%B8%95%E0%B8%B8
# https://www.amarintv.com/news/detail/153044

class linkSpider(CrawlSpider):
    name = "link"
    allowed_domains = ['amarintv.com']
    start_urls = ['https://www.amarintv.com/tags/%E0%B8%AD%E0%B8%B8%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%AB%E0%B8%95%E0%B8%B8',]

    rules = (
        # , deny='detail'
        Rule(LinkExtractor(allow='tags/%E0%B8%AD%E0%B8%B8%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%AB%E0%B8%95%E0%B8%B8')),
        Rule(LinkExtractor(allow='detail'), callback='parse_links')
    )

    def parse_links(self, response):
        yield{
            'Head' : response.css('div.head h1::text').get(),
            'Topic' : response.css('div.body p::text').get(),
            'date' : response.css('div.option::text').get(),
            'tags' : response.css('strong.tag a::text').get(),
        }

# response.css('div.option::text').get()
# response.css('div.head h1::text').get()
# response.css('strong.tag a::text').getall()