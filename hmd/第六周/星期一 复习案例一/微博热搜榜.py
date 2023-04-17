# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :微博热搜榜.py
%Time       :2022/10/31 11:11
"""
import requests
import json
from pymongo import *
import urllib.parse
# url = "https://weibo.com/ajax/statuses/topic_band?sid=v_weibopro&category=all&page=1&count=10"
url = 'https://weibo.com/ajax/statuses/hot_band'
header = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers=header)
resp.encoding = "utf-8"
info = resp.text
page = json.loads(info)
# print(page)
page1 = page["data"]["band_list"]
for item in page1:
    dict1 = {}  # dict1 自定义   {} 必须写   dict() 是一个函数不可以作为字典的名字
    note = item["note"]
    num = item['num']
    link = 'https://s.weibo.com/weibo?q=%23{}%23'.format(note)
    # print(note, num)
    dict1['note'] = note
    dict1['num'] = num
    print(dict1)
    client = MongoClient('localhost',27017)
    db = client.weibo
    info = db.resoubang
    info = info.insert_one(dict1)