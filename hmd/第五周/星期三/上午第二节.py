# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午第二节.py
%Time       :2022/10/26 10:57
"""

import requests
import json
from lxml import html
from pymongo import  *
import  requests
from  lxml import  html
def gooods():
    for i in range(1,6):  # 0是首页1也是首页
        url = f'http://www.bao66.cn/search/web,407,钱包,,{i},5.html'
        res = requests.get(url)
        html1 = html.etree.HTML(res.text)
        all = html1.xpath('//ul[@class="product_box"]/li')
        client =MongoClient("localhost",27017)   # 数据库连接
        db = client.baobao
        data = db.student
        for b in all:
            dict1={}
            name = b.xpath('.//div[@class="indexbox"]//p/@title')
            if name:
                dict1["name"]=name[0]
            else:
                name=''
            title = b.xpath('.//p[@class="code"]/a/text()')
            if title:
                dict1["title"]=title[0]
            else:
                title = ''
            price = b.xpath('.//p[@class="desc_hover"]/a/b/text()')
            if price:
                dict1["price"]=price[0]
            else:
                price=''
            data.insert_one(dict1)
gooods()