# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :2.py
%Time       :2022/9/28 15:31
"""
import requests
# import json
#
# url = "https://accounts.douban.com/j/mobile/login/basic"
# header = {
# "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
# 'Cookie': 'll="108303"; bid=_NITsbiTtRQ; apiKey=; __utma=30149280.763061646.1664351734.1664351734.1664351734.tengxun; __utmc=30149280; __utmz=30149280.1664351734.tengxun.tengxun.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; user_data={%22area_code%22:%22+86%22%2C%22number%22:%2218337749264%22%2C%22code%22:%229123%22}; vtoken=phone_register%20409001bf2a3945abab79fb80d52e6e92; last_login_way=phone; ap_v=0,6.0; __gads=ID=10ebf75bbe77dff7-2253b644bad60080:T=1664352807:RT=1664352807:S=ALNI_MaZO8aCI6RN_YUUd3sP42D7_D-bew; __gpi=UID=000009e9b6ad401e:T=1664352807:RT=1664352807:S=ALNI_MakuKr6XniK4mjZQH5-E2KL6VcTJQ; push_noty_num=0; push_doumail_num=0; __utmv=30149280.26318; __utmt=tengxun; __utmb=30149280.27.10.1664351734; login_start_time=1664353734752'
# }
# data = {
# 'remember':' true',
# 'name': 18337749264,
# 'password': 1234567,
# }
import requests  # 请求
import json  # 序列化

# 错误归纳：
'''''
如果发现啥都请求了还是不行的话，就要考虑是不是headers的问题了，是不是没有cookie，没有UA，是不是没有
'''
url = 'https://accounts.douban.com/j/mobile/login/basic'
data = {
    'remember': 'true',
    'name': '18337749264',
    'password': '6912530',
}
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
'Cookie':'ll="108303"; bid=_NITsbiTtRQ; apiKey=; __utmc=30149280; __utmz=30149280.1664351734.tengxun.tengxun.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gads=ID=10ebf75bbe77dff7-2253b644bad60080:T=1664352807:RT=1664352807:S=ALNI_MaZO8aCI6RN_YUUd3sP42D7_D-bew; __gpi=UID=000009e9b6ad401e:T=1664352807:RT=1664352807:S=ALNI_MakuKr6XniK4mjZQH5-E2KL6VcTJQ; push_noty_num=0; push_doumail_num=0; __utmv=30149280.26318; user_data={%22area_code%22:%22+86%22%2C%22number%22:%2218337749264%22%2C%22code%22:%229230%22}; vtoken=undefined; last_login_way=account; ap_v=0,6.0; __utma=30149280.763061646.1664351734.1664366007.1664369965.3; __utmt=tengxun; __utmb=30149280.5.10.1664369965; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1664369980%2C%22https%3A%2F%2Fwww.douban.com%2Fpeople%2F263184348%2F%3F_i%3D4366028_NITsbi%2C4369976_NITsbi%22%5D; _pk_ses.100001.2fad=*; _pk_id.100001.2fad=239c43092452d714.1664369980.tengxun.1664370017.1664369980.; login_start_time=1664370020832',
}
session = requests.session()
resp = session.post(url, data=data, headers=header)
resp.encoding = 'utf-8'
print(resp.text)
#  登录个人信息
link = 'https://www.douban.com/people/263184348/?_i=4370492_NITsbi'
header1 = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Referer': 'https://www.douban.com/people/263184348/?_i=4370489_NITsbi'

}
res = session.get(link, headers=header1)
print(res.text)
#  家校作业
# url4 = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
# data2 = {
#     'from': 'en',
#     'to': 'zh',
#     'query': 'red',
#     'transtype': 'realtime',
#     'simple_means_flag': '3',
#     'sign': '207046.510967',  # 尽量加引号去做
#     'token': 'b726745d75863fdfa0895ab06b3d5467',
#     'domain': 'common',
# }
# ress = requests.post(url=url4, headers=header, data=data2)
# bb = ress.text
# print(json.loads(bb))