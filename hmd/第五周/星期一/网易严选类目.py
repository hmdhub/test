# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :网易严选类目.py
%Time       :2022/10/24 8:56
"""
import requests
import json
import csv
import re
# 获取网页严选类目信息
# 第一种方法
def get_cate1():
     # 请求信息

     url =  "https://you.163.com/xhr/globalinfo//queryTop.json"
     header = {
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;x64)AppleWebKit/537.36(KHTMLlike Gecko) Chrome/105.0.0.0 Safari/537.36'
     }
     resp = requests.get(url,headers = header)
     resp.enconding = "utf-8"
     info = resp.text
     # print(info)
     # json模块
     data = json.loads(info)
     catelist = data['data']['cateList']
     for item in catelist:
          cate1_name = item['name']
          subCateGroupList = item['subCateGroupList']
          for sub in subCateGroupList:
               cate2_name = sub['name']
               categoryList = sub['categoryList']
               for cate in categoryList:
                 dic = {}
                 cate3_name = cate['name']
                 dic['cate1'] = cate1_name
                 dic['cate2_name'] = cate2_name
                 dic['cate3_name'] = cate3_name
                 print(dic)



     # pass

# 第二种方法
get_cate1()
def get_cate2():
    url = "https://you.163.com/"
    link = "https://you.163.com/item/list?categoryId=1010000&subCategoryId=1037000"
    header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # 请求网页源码
    response = requests.get(url,headers = header)
    # 指定编码格式
    response.encoding = "utf-8"
    # 获取源码信息 变量接收
    resp = response.text
    # print(resp)
    li = re.findall('"cateList": (.*)],',resp)
    # print(li[0]+']')
    info = json.loads(li[0]+']')
    # 取值
    with open('网易严.csv','a+',newline='')as f:
        w = csv.writer(f)
        form = ['一级标题','二级标题','三级标题','网址']
        data = json.loads(info)
        page = resp['data']['cateList']
        for i in page:
            page = i['name']
            a = i['subCateGroupList']
            for j in a:
                page2 = j['name']
                b = j['categoryList']
                id = j['id']
                for h in b:
                    page3 = h['name']
                    k = h['id']
                    superCategoryId = h['superCategoryId']
                    link3 = link.format(superCategoryId)
                    print(page,page2,page3)

pass
# get_cate2()