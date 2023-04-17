# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午  行业网站.py
%Time       :2022/10/27 10:38
"""
import requests
import json
from lxml import html
resp = requests.get("https://top.chinaz.com/hangye/")
html = html.etree.HTML(resp.text)
all = html.xpath('//ul[@class="listCentent"]/li')
print(len(all))
for item in all:
     name = item.xpath('.//h3[@class="rightTxtHead"]/a/@title')
     if name:
         name = name[0]
     else:
         name = ''
     link = item.xpath('.//h3[@class="RtCRateCent"]//span/"text()')
     if link:
         link = link[0]
     else:
         link = ''

     info = item.xpath('.//p[@class="RtCInfo"]/text()')
     if info:
         info = info[0]
     else:
         info = ''
         print(name,link,info)
