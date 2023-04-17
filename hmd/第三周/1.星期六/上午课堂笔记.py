# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午课堂笔记 pymon.py
%Time       :2022/10/12 14:37
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
# tengxun.json 花括号，双引号
# 2.内置模块，不需要安装，可以直接导入使用import json
# 3.内置四个方法 dump()dumps()load()loads()
# load():和 dump（）对文件操作 一般不用
# loads（）和 dumps（）反序列化



# 今日的课堂笔记
# tengxun.json 花括号，双引号
''''
json 键或者值的格式：字段名称（"必须包含在双引号中"）后面加一个引号然后是值
json 的值可以是数字 字符串 逻辑值 数组 对象
'''
# 2.内置模块，不需要安装，可以直接导入使用
'''
也就是说直接import json 即可不需要pip  手动安装

'''
# 3.内置四个方法 dump()dumps()load()loads()
''''
d 开头的用于python 对象的序列化
l开头的用于python  对象的反序列化
fg：表示文件

'''

