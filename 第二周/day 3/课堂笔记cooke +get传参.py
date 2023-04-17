""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/28 9:17
file :课堂笔记.PY
"""""
# 会话控制的练习
'''''
会话维持：
会话维持能够跨请求保持某些参数，最方便是在同一个session实例发出所有的请求之间保持cookie 使用requests.seeion
1.举例说明使用session发送请求
session = requests.session()
resp = session.post(url,data=data)
# 再次发送请求的时候可以直接用session就不需要再次写了（cookie）
'''
import requests # 请求
import json # 序列化
# 错误归纳：
'''''
如果发现啥都请求了还是不行的话，就要考虑是不是headers的问题了，是不是没有cookie，没有UA，是不是没有
'''
url = 'https://accounts.douban.com/j/mobile/login/basic'
data = {
    'remember': 'true',
    'name': '13674937907',
    'password': '200212115623',
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Cookie': 'll="118237"; bid=0KYSO3k_PsE; __gads=ID=037ac3f6db9e09be-22c18e06a5d600ee:T=1663482922:RT=1663482922:S=ALNI_MZGBglO7J-eh-wYfic1t06cZj0OLQ; __gpi=UID=000009cd01b45126:T=1663482922:RT=1663584539:S=ALNI_Mbaftt2dOEbk1nWUZIhpElfsf_Tgw; apiKey=; __utma=30149280.871399132.1663482919.1663584523.1664257306.9; __utmc=30149280; __utmz=30149280.1664257306.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.4.10.1664257306; login_start_time=1664258215303',
}
session = requests.session()
resp  = session.post(url,data=data,headers=header)
resp.encoding='utf-8'
print(resp.text)
#  登录个人信息
link = 'https://www.douban.com/people/263183627/?_i=43527060KYSO3k,43527300KYSO3k'
header1 = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'Referer': 'https://www.douban.com/'

}
res = session.get(link,headers=header1)
print(res.text)





