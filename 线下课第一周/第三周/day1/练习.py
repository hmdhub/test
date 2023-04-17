# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :练习.py
%Time       :2022/10/8 21:56
"""
import json
import requests

url = "https://dc.3.cn/category/get?&callback=getCategoryCallback"
resp = requests.get(url)
a = resp.text
# print(a)  # 渠道所有响应
b = a.replace('getCategoryCallback(', " ").replace(")", " ")
print(b)
