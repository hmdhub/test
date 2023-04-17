# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午课堂笔记.py
%Time       :2022/10/8 11:29
"""
import requests
from lxml import html
url = "http://www.zhubaojie.com/"
resp = requests.get(url)
html = html.etree.HTML(resp.text)  # 转换文本对象
a = html.xpath('//ul[@class="site-menu"]/li/a/text()')
print(a)


import json


s = "中文abc123"
a = json.dumps(s)
print(json.loads(a))

h = "小小 is a dog 1111"
b = json.dumps(h)
print(json.loads(b))

d = {"name":"贺梦迪"}
m = json.dumps(d)
print(json.loads(m))
# json键值对使用时必须使用双引号
# 1.json 花括号，双引号
# 2.内置模块，不需要安装，可以直接导入使用import json
# 3.内置四个方法 dump()dumps()load()loads()
# load():和 dump（）对文件操作 一般不用
# loads（）和 dumps（）反序列化




