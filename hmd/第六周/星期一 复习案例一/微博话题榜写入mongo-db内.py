# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :微博话题榜写入mongo-db内.py
%Time       :2022/10/31 15:17
"""
import requests
import json
import csv
from pymongo import *
import urllib.parse
import pymysql
def __init__(self):
    self.url = "https://weibo.com/ajax/statuses/topic_band?sid=v_weibopro&category=all&page=1&count=10"
    self.header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # 写入mongo_db
    self.client = MongoClient('localhost', 27017)
    self.db = self.client.weibo2
    self.info = self.db.huatibang