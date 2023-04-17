""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/11/8 9:20
file :hotmysql.PY
"""""
from pymongo import  *
from Weibo import  settings
# 创键连接
client = MongoClient(host=settings.host,port=settings.port)
db = client[settings.db]
info = db[settings.info]
class Mon():
    @staticmethod
    def insert2(data):
        info.insert_one(dict(data))