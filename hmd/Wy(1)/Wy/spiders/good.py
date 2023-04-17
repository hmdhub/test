import scrapy
import re
from Wy.items import  WyItem
import  json
class GoodSpider(scrapy.Spider):
    name = 'good'
    allowed_domains = ['you.163.com']
    start_urls = ['https://you.163.com/item/list?categoryId=1005002&subCategoryId=1008015']

    def parse(self, response):
        item = WyItem()
        info = re.findall('var json_Data=(.*)};',response.text)
        new_info = info[0]+'}'
        allinfo =json.loads(new_info)
        # print(allinfo)
        allinfo2 = allinfo["categoryItemList"]
        for m in allinfo2:
                name = m["itemList"]
                for i in name:
                    name=i["name"]
                    price=i["retailPrice"]
                    title = i["simpleDesc"]
                    img = i["listPicUrl"]
                    item['title'] = title
                    item['img'] = img
                    item['price'] = price
                    item['name'] = name
                    # print(name,price,title,img)
                    yield item
        pass
