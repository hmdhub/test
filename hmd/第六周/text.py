# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :text.py
%Time       :2022/10/31 9:43
"""
import requests
import  json
from pymongo import  *
import urllib.parse
url = 'https://weibo.com/ajax/statuses/topic_band?sid=v_weibopro&category=all&page=1&count=10'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
req = requests.get(url,headers = header)
# print(req.text)
info = json.loads(req.text)
# print(info)
all = info["data"]["statuses"]
for item in all:
    dict2 = {}
    name = item["topic"]
    read = item["read"] # 阅读量
    mid = item["mid"] # 评论量
    rename = urllib.parse.quote(name)
    # 解码
    link = f"https://s.weibo.com/weibo?q={rename}&topic_ad="
    rank = item["rank"] # 排名
    lianjieall = item["mblog"]["text"]
    # print(dict2)
    dict2["name"] = name
    dict2['link'] = link
    dict2["paiming"] = rank
    dict2["text"] = lianjieall
    dict2["mid"] = mid
    dict2['read'] = read
    # print(dict2)
    client = MongoClient('localhost', 27017)
    db = client.weibo2
    info = db.huatibang
    info= info.insert_one(dict2)




# 微博复习
import  re
import requests
import  json
import csv
from pymongo import  *
import urllib.parse
import pymysql
class Wb():
    def __init__(self):
        self.url = 'https://weibo.com/ajax/statuses/topic_band?sid=v_weibopro&category=all&page=1&count=10'
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }
        # 写入mongo_db
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.weibo2
        self.info = self.db.huatibang
        # 写入mysql
        self.con = pymysql.connect(user="root",password='123456',host='localhost',port=3306,database='big two') # 创建连接
        self.cur = self.con.cursor()# 创建游标
    def htb(self):
        # 写入mongo_db
        req = requests.get(self.url,headers = self.header)
        # print(req.text)
        info = json.loads(req.text)
        # print(info)
        all = info["data"]["statuses"]
        for item in all:
            dict2 = {}
            name = item["topic"]
            read = item["read"] # 阅读量
            mid = item["mid"] # 评论量
            rename = urllib.parse.quote(name)
            # 解码
            link = f"https://s.weibo.com/weibo?q={rename}&topic_ad="
            rank = item["rank"] # 排名
            lianjieall = item["mblog"]["text"]
            # print(dict2)
            dict2["name"] = name
            dict2['link'] = link
            dict2["paiming"] = rank
            dict2["text"] = lianjieall
            dict2["mid"] = mid
            dict2['read'] = read
            # print(dict2)
            self.info.insert_one(dict2)
        self.client.close() # 关闭连接

    def htb2(self):
        # 写入csv
        req = requests.get(self.url, headers=self.header)
        # print(req.text)
        info = json.loads(req.text)
        # print(info)
        all = info["data"]["statuses"]
        with open('话题榜.csv','w+',encoding="utf_8_sig",newline='') as p: # 注意缩进和writerow([]) 里面写的是列表的格式
            one = csv.writer(p)
            head = ["标题","阅读量","评论量","连接","排名","主题",]
            one.writerow(head)
            for item in all:
                name = item["topic"]
                read = item["read"]  # 阅读量
                mid = item["mid"]  # 评论量
                rename = urllib.parse.quote(name)
                # 解码
                link = f"https://s.weibo.com/weibo?q={rename}&topic_ad="
                rank = item["rank"]  # 排名
                lianjieall = item["mblog"]["text"]
                message = [name,read,mid,link,rank,lianjieall]
                one.writerow(message)
    def htb3(self):
        # 写入mysql
        req = requests.get(self.url, headers=self.header)
        # print(req.text)
        info = json.loads(req.text)
        # print(info)
        all = info["data"]["statuses"]
        for item in all:
            dict2 = {}
            name = item["topic"]
            read = item["read"]  # 阅读量
            mid = item["mid"]  # 评论量
            rename = urllib.parse.quote(name)
            # 解码
            link = f"https://s.weibo.com/weibo?q={rename}&topic_ad="
            rank = item["rank"]  # 排名
            lianjieall = item["mblog"]["text"]
            dict2["name"] = name
            dict2['link'] = link
            dict2["paiming"] = rank
            # dict2["text"] = lianjieall
            dict2["mid"] = mid
            dict2['read'] = read
            # print(dict2["text"])
            data = {k: '"'+str(v)+'"' for k,v in dict2.items()} # {'name': '"年龄带给你的是焦虑还是勇气"',
            sql = f'insert into htb(bname,rank,bread,mid,link)values({data["name"]},{data["paiming"]},{data["read"]},{data["mid"]},{data["link"]});'
            self.cur.execute(sql)
            self.con.commit()
        self.cur.close() # 关闭游标
        self.con.close() # 关闭连接
        # 为啥要加引号原因如下
        '''''insert into htb(name,pm,read,mid,main,link)values(年龄带给你的是焦虑还是勇气,1,229600373,4828403721047685,人生第27年 '''''
weibo = Wb()
# 想要数据写入哪里就调用那个方法即可
# weibo.htb2()
weibo.htb3()

