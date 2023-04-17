# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午课堂笔记 pymon.py
%Time       :2022/10/12 14:39
"""

# 不太建议这么写不能够分层  找到对应的内容
import  requests
from lxml import  html
url = 'https://www.hc360.com/seller/search5.html'
resp = requests.get(url)
resp.encoding='utf-8'
html = html.etree.HTML(resp.text)
pic = html.xpath('//dd[@class="newName"]/a/text()')  # 产品信息
print(pic)
number = html.xpath('//span[@class="seaNewPrice"]/text()') # 价格
# print(number)
for i in number:
    ii = i.replace('\r\n',' ')
    print(ii)
# # 图片
''''
//img[@src]  元素
img/@src   属性值
'''
domin = 'https://www.hc360.com/'
pictures  = html.xpath('//div[@class="picmid pRel"]//img/@src')
print(pictures)
# 目标网址
''''
没改之前的'../k3/M06/1B/89/O6L2459FD582250F213C24679F273BC9D8E.jpg..220x220a.jpg',
http://www.hc360.com/m6/M0B/2A/04/wKhQomK9UmuEal4aAAAAAH0Qr10095.jpg..220x220a.jpg
'''''
for i in pictures:
    new_pictures= i.replace('../',domin)
    print(new_pictures)
