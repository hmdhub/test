# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :mongodb的学习.py
%Time       :2022/10/13 10:41
"""
from pymongo import MongoClient

conn = MongoClient('127.0.0.tengxun', 27017)
db = conn.test
my_set = db.stu
info = {
    #  会自动生成一个id 随机生成  哈希算法
    'no': 1,
    'name': 'cc',
    'age': 22,
}
# my_set.insert_one(info)
# 插入多条
many = [
    {'no':2, 'name':'李四','age':222},
    {'no':3, 'name':'张三','age':21},
    {'no':4, 'name': '狗蛋', 'age': 24},
    {'no':5, 'name': 'ke', 'age': 262},
    {'no':6, 'name': 'mi', 'age': 292},
]
# my_set.insert_many(many)
# 查询
# a =my_set.find_one({'age':21})
# print(a)
b = my_set.find({'age':22})
# for i in b:
    # print(i) # 查询所有的时候需要进行for 循环进行
# 更新
# my_set.update_one({'age':24},{'$set':{'name':'更新后'}}) 更新一条
# 更新多条数据
# my_set.update_many({'age':22},{'$set':{'name':'更新多条'}})
# 删除
my_set.delete_one({'age':222})

conn.close()  # 最后都要关闭连接 可以不用浪费资源

