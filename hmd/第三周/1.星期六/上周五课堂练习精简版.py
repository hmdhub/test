# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上周五课堂练习精简版.py
%Time       :2022/10/13 10:30
"""
#  上周五作业完善  没做完
import requests
from lxml import html

url = 'https://www.hc360.com/'
reap = requests.get(url)
reap.encoding = 'utf-8'
# print(reap.text)
# 找到12个目标节点
html = html.etree.HTML(reap.text)
resp = html.xpath('//dd[@class="aside-dd"]/dl')  # 找到12个目标目录
for q in resp:
    # print(q)
    # 找到一级目录
    one = q.xpath('./dt/span/text()') # 得到一级目录
    # 得到二级目录
    tw = q.xpath('.//dd/dl')
    for b in tw:
        dict = {}
        two = b.xpath('./dt/text()') # 得到二级类目的值  ok
        cate3_list = b.xpath('.//dd')
        for i in  cate3_list:
            three  = i.xpath('./a/text()')
            dict['cate1']=one
            dict['cate2'] = two
            dict['cate3']=three
        print(dict)