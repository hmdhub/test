# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午课堂练习.py
%Time       :2022/10/12 10:16
"""
# 方法一
import  urllib.request
resp = urllib.request.urlopen('https://www.python.org')
html = resp.read().decode('utf-8')
# print(html,'第一中方法')
print(resp.geturl()) #用于获取相应内容的url
print(resp.info()) # 返回页面的原信息
print(resp.getcode()) # 返回 HTTP 请求状态码
# 方法2
from urllib.request import  urlopen
url = 'https://www.python.org'
res = urlopen(url)
a = res.read().decode('utf-8')
# print(a,'第二种方法')
# 复杂的url
import urllib.request
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
req = urllib.request.Request('https://www.jd.com/',headers=header) #  可以放置headers
response = urllib.request.urlopen(req)
html1 = response.read().decode('utf-8')
print(html1)
