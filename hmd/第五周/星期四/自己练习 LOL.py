# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :自己练习 LOL.py
%Time       :2022/10/27 20:40
"""
import requests
from lxml import html
import json
import re
# 请求头信息
url = " https://101.qq.com/"
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 请求网页
response = requests.get(url,headers = header)
response.encoding = "gbk"
res = response.text
print(res)

# 使用json模块
info = json.loads(res)
# info中括号开头要列循环
for item in info:
    name = item['name']
