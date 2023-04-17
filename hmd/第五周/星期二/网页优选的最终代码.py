# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :网页优选的最终代码.py
%Time       :2022/10/25 9:03
"""
# import pymysql
# import requests
# import json
# from lxml import html
# class You(object):
#     def __init__(self):
#         self.url = 'https://you.163.com/xhr/globalinfo//queryTop.json'
#         self.header = {
#             'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#         }
#         # 数据库连接
#         self.conn = pymysql.connect(host='localhost',user='root',password='123456',database='hmd',port=3306)
#         # 获取游标：
#         self.cursor= self.conn.cursor()
#
#         self.goodli = []
#
#     # 得到类目信息
#     def cate(self):
#         # with open('网页优选plus.csv', 'w+', encoding='utf-8', newline="") as f:  # 不可以放进for 循环里面 会手动关闭
#         #     a = csv.writer(f)
#         #     row = ["一级类目", "二级类目", '三级类目','商品名称','商品解读','商品价格','商品图片']
#         #     a.writerow(row)
#             response = requests.get(self.url, self.header)
#             response.encoding = 'utf-8'
#             info = json.loads(response.text)
#             all = info['data']['cateList']
#             for item in all:
#                 dict = {}
#                 id1 = item['id']
#                 one = item['name']  # 一级类目
#                 two = item['subCateGroupList']
#                 for ir in two:
#                     two = ir['name']  # 二级类目
#                     teo = item['subCateList']
#                     for it in teo:
#                         three = it['name']  # 三级类目
#                         id2 = it['id']
#                         dict["one"] = one
#                         dict["two"] = two
#                         dict["three"] = three
#                         # 三级类目的url 拼接
#                         last_url = f'https://you.163.com/item/list?categoryId={id1}&subCategoryId={id2}'
#                         self.good(one,two,three,last_url)
#                         if len(self.goodli) > 0:
#                             for shangpin in self.goodli:
#                                 data = {k:'"'+str(v)+'"' for k,v in shangpin.items()}
#                                 sql = f'INSERT INTO wyy(one,two,three,bname,pic,bprice,title) VALUES ({data["one"]},{data["two"]},{data["three"]},{data["bname"]},{data["pic"]},{data["bprice"]},{data["title"]});'
#                                 # print(sql)
#                                 self.save(sql)
#
#             self.cursor.close()
#             self.conn.close()
#     # 得到商品的信息
#     def good(self,one, two, three, last_url):
#         response = requests.get(last_url, headers=self.header)
#         response.encoding = 'utf-8'
#         a = response.text
#         new_a = a.split('var json_Data=')[tengxun].split('</script>')[0]
#         all_a = new_a.split('json_Data.')[0].replace('}]};', '}]}')
#         # 处理json 数据
#         aa = json.loads(all_a)
#         # print(aa)
#         # 处理数据
#         info = aa['categoryItemList']
#         for item in info:
#             name = item['itemList']
#             for i in name:
#                 dict1 = {}
#                 dict1['bname'] = i['name']  # 名字
#                 dict1['title'] = i['simpleDesc']  # 标题
#                 dict1['pic'] = i['listPicUrl']  # 图片的url
#                 dict1['bprice'] = i['retailPrice']# 商品的价格
#                 dict1["one"] = one
#                 dict1["two"] = two  # 循环外面
#                 dict1["three"] = three
#                 self.goodli.append(dict1)
#     def save(self,sql):
#         self.cursor.execute(sql)
#         # 提交数据
#         self.conn.commit()
#
#     # 解析
# H = You()
# H.cate()

import requests
import re
import json
import pymysql
class Wyyx(object):
    def __init__(self):
        self.url = 'https://you.163.com/xhr/globalinfo//queryTop.json?__timestamp=1666580488414'
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }
        # 三级类目的链接
        # https://you.163.com/item/list?categoryId=1005000&subCategoryId=109323000
        # https://you.163.com/item/list?categoryId=1005000&subCategoryId=109323024
        self.link = 'https://you.163.com/item/list?categoryId={}&subCategoryId={}'
        self.good_li = []
        # 建立数据库连接
        self.conn = pymysql.connect(
            host="127.0.0.tengxun",
            user='root',
            password='123456',
            database='hmd',
            port=3306
        )
        # 获取游标
        self.cursor = self.conn.cursor()
        pass
    # 目录信息
    def get_cate(self):
        # 请求网页
        response1 = requests.get(self.url, headers=self.header)
        response1.encoding = 'utf-8'
        info = response1.text
        # print(info)
        # json模块
        data = json.loads(info)
        cateList = data['data']['cateList']
        for item in cateList:
            cate1_name = item['name']
            subCateGroupList = item['subCateGroupList']
            for sub in subCateGroupList:
                cate2_name = sub['name']
                categoryList = sub['categoryList']
                for cate in categoryList:
                    cate3_name = cate['name']
                    superCategoryId = cate['superCategoryId']
                    id = cate['id']
                    # 拼接三级目录的链接
                    cate3_link = self.link.format(superCategoryId, id)
                    # 调用商品的方法
                    self.get_good(cate1_name, cate2_name, cate3_name, cate3_link)

                    if len(self.good_li) > 0:
                        for i in self.good_li:
                            data1 = {k: '"' + str(v) + '"' for k, v in i.items()}
                            # 写sql语句
                            sql = f'INSERT INTO wyy(one,two,three,bname,pic,bprice,title) VALUES({data["one"]},{data[ "two"]},{data["three"]}, {data["bname"]}, {data["pic"]}, {data["bprice"]},{data["title"]});'

                            print(i)
                            self.save(sql)
        self.cursor.close()
        self.conn.close()

        pass
    # 从三级目录中进入，获取商品信息
    # 商品信息
    def get_good(self, cate1, cate2, cate3, cate3_link):
        # 请求网页
        response = requests.get(cate3_link, headers=self.header)
        # 指定编码格式
        response.encoding = 'utf-8'
        # 输出响应文本
        page = response.text
        # print(page)
        # 运用正则匹配所需字符串
        res = re.findall('var json_Data=(.*)};', page)
        # print(res[0])
        text = res[0] + '}'
        # json数据类型转化
        data = json.loads(text)
        print(type(data))  # <class 'dict'>
        # 字典取值
        categoryItemList = data['categoryItemList']
        for item in categoryItemList:
            itemList = item['itemList']
            for i in itemList:
                good = {}
                name = i['name']
                simpleDesc = i['simpleDesc']
                retailPrice = i['retailPrice']
                scenePicUrl = i['scenePicUrl'] + '?type=webp&imageView'
                good['name'] = name
                good['des'] = simpleDesc
                good['price'] = retailPrice
                good['img'] = scenePicUrl
                good['cate1'] = cate1
                good['cate2'] = cate2
                good['cate3'] = cate3
                # 商品图片链接
                # "https://yanxuan-item.nosdn.127.net/3ad6d24736c143cccc2c2bd02d6fa72a.jpg"
                # "https://yanxuan-item.nosdn.127.net/b7d5a39aca6b0bf27991d2f6ef30f071.jpg?type=webp&imageView"
                # 每次把商品追加到good_li列表中
                self.good_li.append(good)
        pass
    def save(self, sql):
        # 执行sql语句
        # 插入语句
        self.cursor.execute(sql)
        # 提交数据
        self.conn.commit()
        # 关闭游标
        # conn.close()
# 实例化对象
wy = Wyyx()
# 调用方法
wy.get_cate()

