# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :下午课堂练习.py
%Time       :2022/9/30 17:50
"""
# xpath慧聪网练习
import requests
from lxml import html
url = "https://www.hc360.com/"
header = {
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
resp = requests.get(url)
resp.encoding = 'utf-8'
html = html . etree.HTML(resp.text)
# 一级内容
a = html.xpath('//dt[@class="sub-menu-dt"]/span/text()')
print(a)
# 二级内容
b =  html.xpath('//dd[@class="sub-menu-dd"]/dl/dt/text()') # dl dt 不可弄反
print(b)
# 三级内容
c = html.xpath('//dd [@class="sub-menu-dd"]/dl//a/text()')
print(c)