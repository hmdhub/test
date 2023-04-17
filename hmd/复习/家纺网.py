# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :家纺网.py
%Time       :2022/11/23 11:03
"""

import requests
import csv
import pymysql
from pymongo import *
from lxml import html
url = "http://www.91jf.com/"
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=header)
info = resp.text
ht = html.etree.HTML(info)
all = ht.xpath('//div[@class="index_g_class"]/ul/li')
print(all)
# 把all进行循环 获取all里面的信息
for i in all:
    one = i.xpath('.//div[@class="class_menu"]/a/span/text()')[0]
    two = i.xpath('.//div[@class="class_menu"]/a/text()')[0]
    three = i.xpath('.//div[@class="class_child"]/div[@class="class_child_li"]/ul/li')
    for j in three:
        dict1 = {}
        three = j.xpath('.//a/span/text()')[0]
        link = j.xpath('.//a/@href')[0]
        link_url = url + link
        dict1["cate1_name"] = one
        dict1["cate2_name"] = two
        dict1["cate3_name"] = three
        dict1["link_url"] = link_url
        print(dict1)

# # 写入csv
# with open('info.csv','w+',newline='') as f:
#     a = csv.writer(f)
#     for item in all:
#         one = item.xpath('.//div[@class="class_menu"]//a/span/text()')
#         two = item.xpath('.//a/text()')
#         three = item.xpath('.//div[@class=""class_child_li"]//a//span/text)')
#         # info = [one,two,three]
#         print(one,two,three)
#         a.writerow(info)