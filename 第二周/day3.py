# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :day3.py
%Time       :2022/9/28 9:39
"""
import requests
import json
# 方法一
header = {
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0Safari/537.36'
}
url = "http://httpbin.org/get?name=张三&age=18"
response = requests.get(url,headers = header)
res = response.text
print(json.load(res))

# 方法二





# post 请求
url1 = "http://httpbin.org/post"
data = {
    "name":"python"
}
resp = requests.post(url1,data=data,headers=header)
print(resp.text)



url2 = "https://fanyi.baidu.com/translate?"
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

}
data = {

'from': 'en',
'to': 'zh',
'query': 'do',
'transtype': 'realtime',
'simple_means_flag': 3,
'sign': 602137.906024,
'token': 'a5973ea3138352d0aeacbb4614a2f02c',
'domain': 'common'
}
res = requests.post(url=url2,headers=header,data=data)
a = res.text
print(json.load(a))