import scrapy
import  json
import re
from Wy.items import WyItem
class GoodsSpider(scrapy.Spider):
    name = 'goods'
    allowed_domains = ['you.163.com']
    start_urls = ['https://you.163.com/xhr/globalinfo//queryTop.json?__timestamp=1667806947451']

    def parse(self, response):
        item = WyItem()
        info = json.loads(response.text)
        message = info["data"]["cateList"]
        for i in message:
            one = i["name"]
            tw = i["subCateGroupList"]
            for it in tw:
                two = it['name']
                thr = it["categoryList"]
                for ite in thr:
                    three = ite["name"]
                    item["one"] = one
                    item["two"] = two
                    item["three"] = three
                    yield  item

                    #
                    # print(one,two,three)
        pass
