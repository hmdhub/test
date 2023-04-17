import scrapy
import requests
import json
import urllib.parse


class ResouSpider(scrapy.Spider):
    name = 'Resou'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']

    def parse(self, response):
        all = json.loads(response.text)
        info =all["data"]["realtime"]
        for item in info:
            # dict1 = {}
            name = item["note"]

            i = urllib.parse.quote(name)
            link = f'https://s.weibo.com/weibo?q=%23{}%23&topic_ad='.format(i)
            rank = item["realpos"]
            
            print(name,rank,link)

            yield {
                '标题',name,
                '排名',rank,
                '链接',link
            }
        pass
