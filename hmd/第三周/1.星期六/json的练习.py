# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :json的练习.py
%Time       :2022/10/13 10:33
"""

#  header
import json
import requests

url = 'https://dc.3.cn/category/get?&callback=getCategoryCallback'
reap = requests.get(url)
# reap.encoding='utf-8' # 此时此刻是不需要编码
a = reap.text
# print(type(a))
# print(json.loads(a))
b = a.replace("getCategoryCallback(", " ").replace(")", " ")
c = json.loads(b)
# print(c)
d = c['data']
for i in d:
    pp = i['s']
    for a in pp:
        name = a['s']
        print(name)

        for i in name:
            aa = i['n']
            print(aa)
            b = aa.split('|')[1]  # 拿到所有的二级目录 没有问题