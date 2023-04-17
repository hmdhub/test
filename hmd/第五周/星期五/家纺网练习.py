# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :家纺网练习.py
%Time       :2022/10/28 16:35
"""
import requests
from lxml import html
import json
url = "http://detail.91jf.com/goods/7hu49f3"
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers = header)
ht = html.etree.HTML(resp.text)
a = resp.text
print(a)
# price = ht.xpath("//span[@class="price_info fl price_info_detail"]/span/text()")