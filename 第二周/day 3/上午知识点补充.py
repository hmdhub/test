""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/29 9:48
file :上午知识点补充.PY
"""""
url = 'http://httpbin.org/get'
import requests
# requests的方法
req = requests.get(url)
print(req.text)#
# requests的一些属性和方法
print(req.json())
print('**********************')
print(req.headers) # 以字典对象存储服务器的响应头，不区分大小写
print(req.url) # 获取请求的网址
# print(req.Cookie)  # 获取请求后的cookie