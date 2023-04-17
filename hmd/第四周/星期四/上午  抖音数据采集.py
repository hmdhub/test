# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午  抖音数据采集.py
%Time       :2022/10/20 10:25
"""
import requests
from lxml import html
import json
import csv
url = "https://www.douyin.com/"
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=header)
print(resp)   # 得到json数据  需要反序列化
new_data = json.loads(resp.text)
print(new_data)
for item in new_data['list']:
    data = item['title']
    if data == "抖音热榜":
        new = item['cards']
        print(new)
        for k in new:
            print(k)
            yellow = k['hotspot']['hot_word']
            new_yellow = yellow.split(',')[0].replace('{"Word":','')
            title = k['hotspot']['top_aweme_raw']
            new_title = title.split(',',)[1].replace('"desc":','')
            baose = title.split(':')[6].replace(',"avatar_larger"','')
            print(baose,new_yellow,new_title)
            with open('data.csv','a+') as p:
                a = csv.writer(p)
                bb = [baose,new_title,new_yellow]
                a.writerow(bb)


