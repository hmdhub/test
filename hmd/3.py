# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :3.py
%Time       :2022/9/27 14:36
"""
import  requests
url = "http://www.jd.com"
response = requests.get(url)
print(response.text)



import  urllib.request
import  urllib.parse
import  json
url = 'https://accounts.douban.com/j/mobile/login/basic?remember=true&name=13674937907&password=1111'
data = {
'remember': 'true',
'name': '13674937907',
'password':' 1111',
'ticket': 't03tVAoQK7BfI9dYWZFV77Ht8TfSkrcO3_cxZNYOuoHvivvub5j5OZIa5-iu2vLJRbHSLjdfJAE7kCY4ibRoH3pEVthPAFJoi_h3iNfqdWudBORGJIGJxFwxNJ7PHuFYM3i21bP5m8vcmCqCmR-l-G_A5Wv250XpuhfULk4N6f-h8gOB3MgtdtBDV6Q9GkHT-qx',
'randstr': '@2cZ',
'tc_app_id':'2044348370'
}
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'Cookie':'ll="118237"; bid=0KYSO3k_PsE; __gads=ID=037ac3f6db9e09be-22c18e06a5d600ee:T=1663482922:RT=1663482922:S=ALNI_MZGBglO7J-eh-wYfic1t06cZj0OLQ; __gpi=UID=000009cd01b45126:T=1663482922:RT=1663584539:S=ALNI_Mbaftt2dOEbk1nWUZIhpElfsf_Tgw; apiKey=; __utma=30149280.871399132.1663482919.1663584523.1664257306.9; __utmc=30149280; __utmz=30149280.1664257306.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=tengxun; __utmb=30149280.4.10.1664257306; login_start_time=1664258215303',
}
info = bytes(urllib.parse.urlencode(data).encode('utf-8'))
resp = urllib.request.Request(url,data=info,headers=header)
response = urllib.request.urlopen(resp)
a = response.read().decode('utf-8')
print(a)