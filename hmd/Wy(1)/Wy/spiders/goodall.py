import scrapy


class GoodallSpider(scrapy.Spider):
    name = 'goodall'
    allowed_domains = []
    start_urls = ['']

    def parse(self, response):
        pass
