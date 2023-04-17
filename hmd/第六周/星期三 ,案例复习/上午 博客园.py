# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午 博客园.py
%Time       :2022/11/2 8:32
"""
import requests
import csv
from lxml import html
import json
"""
注意：
1.post请求
2.请求头信息还需要content-type
3.post 请求参数需要序列化
"""
# 写入csv中
# 请求地址
with open("bokeyuan.csv", 'w+', newline='', encoding="utf_8_sig") as f:
    obj = csv.writer(f)
    row = ['课程名字', '课程链接']
    obj.writerow(row)
    url = 'https://www.cnblogs.com/AggSite/AggSitePostList'
    # 请求头信息
    header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'content-type': 'application/json; charset=UTF-8'
        }
    # post 请求携带的参数（pageIndex变化参数）
    # 翻页
    for i in range(1, 4):
        data = {
                "CategoryType":"SiteHome",
                "ParentCategoryId":0,
                "CategoryId":808,
                "PageIndex":int(i),
                "TotalPostCount":4000,
                "ItemListActionName":"AggSitePostList"
            }
        resp = requests.post(url, headers=header,data=json.dumps(data))
        resp.encoding = 'utf-8'
        res = resp.text
        # print(resp.status_code)
        # print(res)
        page = html.etree.HTML(res)
        article_li = page.xpath('//article[@class="post-item"]')
        for item in article_li:
            name = item.xpath('.//a[@class="post-item-title"]/text()')[0]
            link = item.xpath('.//a[@class="post-item-title"]/@href')[0]
            info = [name, link]
            obj.writerow(info)
            # print(name,link)


