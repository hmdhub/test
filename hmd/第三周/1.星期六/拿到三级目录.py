# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :拿到三级目录.py
%Time       :2022/10/13 10:29
"""
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
        # print(name)
        for i in name:
            aa = i['s']  # 找到所有的三级目录
            for q in aa:
                qq = q['n']
                qq = qq.split('|')[1]
                print(qq)
