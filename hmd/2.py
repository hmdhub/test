# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :2.py
%Time       :2022/9/27 8:49
"""
import urllib.request
import  urllib.parse
import json
# 构造request对象
# 一
url = "https://fanyi.baidu.com/sug"
header = {
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
date = {
    "kw": "red"
}
info = bytes(urllib.parse.urlencode(date).encode('utf-8'))
requests = urllib.request.Request(url,data = info,headers=header)
response = urllib.request.urlopen(requests)
a = response.read().decode('utf-8')
print(json.loads(a))

#二
url = "https://fanyi.baidu.com/sug"
url2 = "https://fanyi.baidu.com/langdetect"
header = {

'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
# 用input随意查询单词
b = input("请输入你想要的单词")
date = {
    "kw": b
}
info = bytes(urllib.parse.urlencode(date).encode('utf-8'))
requests = urllib.request.Request(url,data = info,headers=header)
response = urllib.request.urlopen(requests)
a = response.read().decode('utf-8')
print(json.loads(a))