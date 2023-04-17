# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :下午2.py
%Time       :2022/10/12 10:17
"""
import  requests
'''
解释requests.get(url,params,**kwargs,return,retype)中的参数
url ：就是要访问的目标对象网址
params和**kwargs 均为可选参数
params的数据类型是dict ,tuple list bytes(字节)的类型
**kwargs:可选参数
return :返回的是Response响应
retype:数据类型(requests.response)
'''
url = 'https://www.jd.com'
response1 = requests.get(url)
# print(response.text)
url = 'http://www.baidu.com'
response2 = requests.get(url)
response2.encoding='utf-8'
# print(response.text)
#  带参数请求两种方法
# 第一种方法
url1 = 'https://www.baidu.com/s?wd=河南艺术职业学院'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
response = requests.get(url1,headers=headers)
# print(response.text)
# 第二种方法
url = 'https://www.baidu.com/s'
par = {
    'wd':'河南艺术职业技术学院'
}
response3 = requests.get(url,params=par,headers=headers)
print(response3.text)