# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午  行业网站.py
%Time       :2022/10/26 8:35
"""
import requests
import json
from pymongo import *
from lxml import html
def all():
    url  = "https://www.bao66.cn/web/"
    header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)      Chrome/105.0.0.0 Safari/537.36'
}
    resp = requests.get(url,headers=header)
    resp.encoding = "utf-8"
    page = resp.text
    print(page)
    print(resp.url)

    # 获取商品的标题、简介、价格 第一页内容
    # xpath
def goods():
    # 查看五页内容  页面拼接
    for i in range(1,6):
        url = f'http://www.bao66.cn/search/web,407,钱包,,{i},5.html'

        # url = "http://www.bao66.cn/search/web,407,0,,1,5.html"
        header = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
         }
        # 请求网页
        resp = requests.get(url,headers=header)
        # a = resp.text
        # print(a)
        ht = html.etree.HTML(resp.text)
        all = ht.xpath('//ul[@class="product_box"]')
        # print(len(all))
        client = MongoClient("localhost",27017)
        db = client.mongo_hmd
        data = db.stu
        for item in all:  # 只打印第一页内容
            dict = {}
            name = item.xpath('.//div[@class="indexbox"]//p/@title')  # 标题
            # 判断
            if name:
                dict["name "]= name[0]
            else:
                name = ''
            title = item.xpath('.//p[@class="code"]/a/text()')    # 简介
            if title:
               dict ["title"] = title[0]
            else:
                title = ''
            price = item.xpath('.//p[@class="desc_hover"]/a/b/text()')   # 价格
            if price:
                dict ["price"] = price[0]
            else:
                price = ''
            print(name,title,price)

            data.insert_one(dict)

goods()













