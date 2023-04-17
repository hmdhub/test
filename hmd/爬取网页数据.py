# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :爬取网页数据.py
%Time       :2022/9/26 10:45
"""
import urllib.request
response = urllib .request.urlopen("https://www.python.org")
html = response.read().decode("UTF-8")
# print(html)
print(response.geturl())
print(response.getcode())
print(response.info())


# 构造Rquest对象
import  urllib.request
header = {
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.'
}
req = urllib.request.Request("http://www.baidu.com",headers=header)

response = urllib.request.urlopen(req)
html = response.read().decode("UTF-8")
print(html)


import  urllib.request
header = {
'user-agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
req = urllib.request.Request("http://www.jd.com",headers=header)

response = urllib.request.urlopen(req)
html = response.read().decode("UTF-8")
print(html)


