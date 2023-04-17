import scrapy
import requests
import json
import re
import pymysql

class WySpider(scrapy.Spider):
    name = 'wy'
    allowed_domains = ['163.com']
    start_urls = ['https://you.163.com/xhr/globalinfo//queryTop.json?__timestamp=1667807540159']
   
    def parse(self, response):
        dict1 = {}
        info = json.loads(response.text)
        # print(info)
        message = info["data"]["cateList"]
        for item in message:
            cate1_name = item['name']
            item1 = item['subCateGroupList']
            for sub in  item1:
                cate2_name = sub['name']
                item2 = sub['categoryList']
                for cate in  item2:
                    cate3_name = cate['name']
                    item3 = cate['superCategoryId']
                    id = cate['id']
                    # 拼接三级目录的链接
                    # self.link = 'https://you.163.com/item/list?categoryId={}&subCategoryId={}'
                    # self.good_li = []
                    # cate3_link = self.link.format( item3, id)
                    # print(cate1_name, cate2_name, cate3_name, cate3_link)
                    dict1["cate1_name"] = cate1_name
                    dict1["cate2_name"] = cate2_name
                    dict1["cate3_name"] = cate3_name
                    # dict1["cate3_link"] = cate3_link
                    yield dict1
                pass
