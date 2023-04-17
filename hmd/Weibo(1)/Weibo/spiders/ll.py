import scrapy
import urllib.parse
import json

class LlSpider(scrapy.Spider):
    name = 'll'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.com/ajax/side/hotSearch']
    def parse(self, response):
        infoall = json.loads(response.text)
        info = infoall["data"]["realtime"]  # ["band_list"]  # 有问题
        for it in info:
            name = it["word"]
            if name:
                name = name
            else:
                name = ''
            a = urllib.parse.quote(name)
            link = f'https://s.weibo.com/weibo?q=%23{a}%23&topic_ad='
            rank = it["realpos"]
            if rank:
                rank = rank
            else:
                rank = ''
            if link:
                link = link
            else:
                link = ''
            yield {
                "热搜词": name,
                "排名": rank,
                "链接": link,
            }
