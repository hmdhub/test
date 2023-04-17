# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :微博话题榜.py
%Time       :2022/10/31 8:52
"""
import requests
import json
from pymongo import *
import urllib.parse
url = "https://weibo.com/ajax/statuses/topic_band?sid=v_weibopro&category=all&page=1&count=10"
header = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=header)
# resp.encoing = "utf-8"
page = resp.text
# print(page)
info = json.loads(page)
# print(info)
all = info['data']['statuses']
for s in all:
    dict = {}  # 列表
    name = s["topic"]
    read = s["read"]  # 阅读量
    mid = s["mid"]  # 评论量
    rename = urllib.parse.quote(name)
    # 解码
    # link =  f"https://s.weibo.com/weibo?q={rename}&topic_ad="
    link = 'https://s.weibo.com/weibo?q=%23{}%23'.format(name)
    rank = s["rank"]  # 排名
    lianjieall = s["mblog"]["text"]
    # print(name,read,mid,rank,lianjieall)
    dict['name'] = name
    dict['paiming'] = rank
    dict['link'] = link
    dict['mid'] = mid
    dict['read'] = read
    dict['text'] = lianjieall
    client = MongoClient('localhost',27017)
    db = client.weibo
    info = db.huatibang
    info = info.insert_one(dict)





















