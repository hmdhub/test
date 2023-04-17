# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :京东.py
%Time       :2022/10/14 11:16
"""
import requests
from lxml import html
import csv

url = "https://www.jd.com/"
header = {
'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 请求页面
response = requests.get(url,header=header)
# 打印网页源源码
print(response.text)
# 解析数据
ht = html.etree.HTML(response.text)
# 一级类目
# one = ht.xpath("//ul[@class="JS_navCtn cate_menu"]//li/a/text()")
one = ht.xpath('div//[@id="J_cate"]//li/a/text()')
print(one)
with open('jd.csv','a+')as f:
    n = csv.writer(f)
    n.writerrow(one)
