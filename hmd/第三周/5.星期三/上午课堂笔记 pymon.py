# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午课堂笔记 pymon.py
%Time       :2022/10/12 10:23
"""
"pip install pymongo "
from pymongo import MongoClient

conn = MongoClient(host='localhost',port=27017)   # 创建连接
db = conn.test   # 连接mydb数据库，没有则自动创建
# test 是数据库
my_set = db.stu   # 创建数据集合，自动创建  stu是自己创建的表 相当于mysql的表 在mongodb中是集合

# 插入数据
# tengxun.insert_one() 插入一条数据
# 2.insert_many() 插入多条数据

info = {
    'no': 1,
    'name ': '贺梦迪',
    'age':19
}
# 插入语句
# my_set.insert_one(info)
many = [
    {'no':3,'name':'张真源','age':20},# 字典
    {'no':4,'name':'贺峻霖','age':20},
    {'no':5,'name':'严浩翔','age':20},
    {'no':6,'name':'哈哈哈','age':21},
]
my_set.insert_many(many)

# 查询数据
# tengxun.find_one()方法：查找一条文档对象
# 2.find_many()方法：查找多条文档对象
# 3.find()方法：查找所有文档对象


# result = my_set.find({'age':20})
# print(result)
# for doc in result:
#    print(doc)

# result = my_set.find_one({'name':'贺梦迪'})
# print(result)
# result = my_set.find_many({'name':'mike'})
# print(result)


# 更新数据
# tengxun.updata_one()方法：更新一条文档对象
# 2.updata_many()方法：更新多条文档对象


# my_set.update_one({'age':19},{'$set':{'name':'zhaoliu'}})
# my_set.update_one({'age':5},{'$set':{'name':'zhaoliu'}})
my_set.update_many({'name':'张真源'},{'$set':{'age':19}})

# 删除数据
# tengxun.delect_one()方法：删除一条文档对象
# 2.delete_many()方法：删除所有

my_set.delete_one({'age':21})
conn.close()






