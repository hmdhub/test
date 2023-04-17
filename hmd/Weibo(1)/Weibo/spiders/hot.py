import scrapy
import  urllib.parse
import  json
from  Weibo.items import WeiboItem
class HotSpider(scrapy.Spider):
    name = 'hot'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.com/ajax/side/hotSearch']
    def parse(self, response):
        infoall = json.loads(response.text)
        info = infoall["data"]["realtime"]   #["band_list"]  # 有问题
        for it in info:
            item = WeiboItem()
            name =it["word"]
            if name:
                name = name
            else:
                name = ''
            a=urllib.parse.quote(name)
            link = f'https://s.weibo.com/weibo?q=%23{a}%23&topic_ad='
            # rank = it["realpos"]
            # if rank:
            #     rank = rank
            # else:
            #     rank = ''
            if link:
                link = link
            else:
                link = ''
            item["name"] = name
            item["link"] = link
            # item["rank"] = rank
            yield item
    #         # print(a)
    #         # yield {
    #         #     "热搜词":name,
    #         # "排名":rank,
    #         # "链接":link,
    #         # }
    #
    # '%E6%B6%88%E8%B4%B9%E8%80%85%E7%A7%B0%E6%9D%8E%E4%BD%B3%E7%90%A6%E7%9B%B4%E6%92%AD%E9%97%B4%E4%BA%A7%E5%93%81%E6%AF%94%E5%AE%98%E6%96%B9%E8%B4%B5'  # link 编码的效果
    # 'https://s.weibo.com/weibo?q=%23%E6%B6%88%E8%B4%B9%E8%80%85%E7%A7%B0%E6%9D%8E%E4%BD%B3%E7%90%A6%E7%9B%B4%E6%92%AD%E9%97%B4%E4%BA%A7%E5%93%81%E6%AF%94%E5%AE%98%E6%96%B9%E8%B4%B5%23&topic_ad='
    # '%23消费者称李佳琦直播间产品比官方贵%23'
    # # print(name,link,rank)
    # "https://s.weibo.com/weibo?q=%23%E6%B6%88%E8%B4%B9%E8%80%85%E7%A7%B0%E6%9D%8E%E4%BD%B3%E7%90%A6%E7%9B%B4%E6%92%AD%E9%97%B4%E4%BA%A7%E5%93%81%E6%AF%94%E5%AE%98%E6%96%B9%E8%B4%B5%23&topic_ad"