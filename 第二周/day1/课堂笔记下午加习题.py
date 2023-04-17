""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/25 18:19
file :课堂笔记.PY
"""""
import  urllib.request
import  urllib.parse
dic = {
    '爱好':'吃辣条',
    '班级':'一班'
}
info =urllib.parse.urlencode(dic)#编码
print(info)
# 解码
result = urllib.parse.unquote('%E7%88%B1%E5%A5%BD=%E5%90%83%E8%BE%A3%E6%9D%A1&%E7%8F%AD%E7%BA%A7=%E4%B8%80%E7%8F%AD')
print(result)
url = 'https://www.baidu.com/s'
word = {
    "wd": '河南艺术职业学院'
}
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
# req = urllib.request.Request('https://www.baidu.com/',headers=header) #  里面可以放置headers
word = urllib.parse.urlencode(word)  # 编码
new_html = url+"?"+word
# 构造复杂的Requests对象
req1 = urllib.request.Request(new_html,headers=header) # 里面可以放置header
resp = urllib.request.urlopen(req1)
htmll = resp.read().decode('utf-8') # 注意decode一般在响应的时候解码
print(htmll)