# -*- encoding:utf-8 -*-
# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :one.py
%Time       :2023/2/20 10:19
"""
# 30条数据
# import  os
# import  requests
# from lxml import  html
# url = 'https://b.faloo.com/y_0_1.html'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
# info = requests.get(url, headers)
# all = info.text
# # 建立文档树对象
# ht = html.etree.HTML(all)
# if not os.path.exists('./img'):
#     os.mkdir('./img')
# #  拿到所有的标题
# infomation = ht.xpath('//div[@class="centerTwo bodyBorderShadow"]/div[@id="BookContent"]//div[@class="TwoBox02_02"]')
# for item in infomation:
#     title = item.xpath('.//div[@class="TwoBox02_03"]//a/@title')[0]
#     img = item.xpath('.//div[@class="TwoBox02_03"]//img/@src')[0]
#     pic = requests.get(img)
#     if pic.status_code == 200:  # 去请求每一个图片通过响应状态码看是否可以访问到 如果可以就可以下载图片
#         with open('./img/' + str(title) + '.jpg', 'wb')as p:
#             p.write(pic.content)  # 使用字节


# 15条数据
import csv
from lxml import html
import requests
url = "https://b.faloo.com/y_0_1.html"
headers = {
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 建立文档数对象
res = requests.get(url,headers)
ht = html.etree.HTML(res.text)
cate = ht.xpath('//div[@class="TwoBox02_01"]')
for i in cate:
    title = i.xpath('.//h1/a/text()')[0]
    img = i.xpath('.//a/img/@src')[0]
    print(img,title)

