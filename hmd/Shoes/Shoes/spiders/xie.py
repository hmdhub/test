import scrapy
import requests

class XieSpider(scrapy.Spider):
    name = 'xie'
    allowed_domains = ['www.go2.cn']

    start_urls = [f'http://www.go2.cn/search/all/page{i}.html?category_id=all&search_1=1&q=%E5%8D%95%E9%9E%8B&kl=hot'for i in range(1,5)]
    # 翻页
    # 'http://www.go2.cn/search/all/page4.html?category_id=all&search_1=1&q=%E5%8D%95%E9%9E%8B&kl=hot'
    # 'http://www.go2.cn/search/all/page6.html?category_id=all&search_1=1&q=%E5%8D%95%E9%9E%8B&kl=hot'

    def parse(self, response):
        all = response.xpath('//ul[@class="clearfix"]/li[@class="pro-222-three find-similar-item "]')
        for i in all:
            dict1 = {}   # 写入csv
            img =i.xpath('.//img/@src').extract()[0]
            name = i.xpath('.//div[@class="cont-wrap"]//div[@class="pro-name app-text-nowrap"]/text()').extract()[0]
            link = i.xpath('.//a/@href').extract()[0]
            imgall = f'http://www.go2.cn{img}'
            linkall = f'http://www.go2.cn{link}'
            price = i.xpath('.//span[@class="price"]/text()').extract()[0]
            introduce = i.xpath('.//div[@class="cont-wrap"]/div[@class="pro-info app-text-nowrap"]/text()')
            # print(imgall,linkall,price,name,introduce)
            dict1["name"] = name    # 写入csv
            dict1["imgall"] = imgall
            dict1["linkall"] = linkall
            dict1["price"] = price
            dict1["introduce"] = introduce
            yield dict1

            pass
