# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :课堂练习百度翻译.py
%Time       :2022/10/12 10:19
"""
# 前提是有网1
import  urllib.request
import  json
import  urllib.parse
url = 'https://fanyi.baidu.com/sug'
aa = input('请输入要查询的单词')
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
data = {
'kw': aa
}
infomation = bytes(urllib.parse.urlencode(data).encode('utf-8'))
#  构造复杂的Requests 对象传递headers的值
resp = urllib.request.Request(url,headers = header,data = infomation)
response = urllib.request.urlopen(resp)
a = response.read().decode('utf-8')
# print(a) # 没有解码
# 把前端的数据json转换为字典的形式
print(json.loads(a))
