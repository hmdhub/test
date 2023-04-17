# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午课堂练习.py
%Time       :2022/10/8 11:43
"""
import  json
import  requests
url = 'https://dc.3.cn/category/get?&callback=getCategoryCallback'
reap  = requests.get(url)
a = reap.text
# print(json.loads(a))
b = a.replace("getCategoryCallback("," ").replace(")"," ")
c = json.loads(b)
d = c['data']
for i in d:
    pp = i['s']
    for a in pp:
        name = a['s']
        # print(name)
        for i in name:
            aa = i['n']
            b = aa.split('|')[1]
            print(b)