# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :微博数据采集.py
%Time       :2022/10/20 11:21
"""
# import requests
# import csv
# import json
# from lxml import html
# url = "https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F"
# header = {
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
# }
# #  请求页面
# resp = requests.get(url,headers=header)
# # 指定编码
# # response.encoding = 'utf-8'
# a = resp.text
# # all = json.loads(a)
# print(a)
# # 使用json模块
# page = json.loads(a)
# # 字典取值
# realtime = page['data']['realtime']  # 列表
# for item in realtime:
#     title = item['word']
#     category =








