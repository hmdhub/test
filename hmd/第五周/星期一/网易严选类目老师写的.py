import requests
import json
import re
#获取网页严选类目信息
def get_cate1():
    # 请求信息
    url = 'https://you.163.com/xhr/globalinfo//queryTop.json'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    #请求网页
    res = requests.get(url,headers = header)
    res.encoding = 'utf-8'
    info = res.text
    # print(info)
    #json模块
    data = json.loads(info)
    # 字典取值
    cateList = data['data']['cateList']
    for item in cateList:
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
                # print(dic)
    # pass
# get_cate1()
def get_cate2():
    url = 'https://you.163.com/'
    link = 'https://you.163.com/item/list?categoryId={}&subCategoryId={}'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    #请求网页源码
    response = requests.get(url,headers = header)
    #指定编码格式
    response.encoding = 'utf-8'
    #获取源码信息
    res = response.text
    # print(res)
    li = re.findall('"cateList": (.*)],',res)
    # print(li[0]+']')
    info = json.loads(li[0]+']')
    #取值
    for item in info:
        cate1 = item['name']
        subCateList = item['subCateList']
        for sub in subCateList:
            cate3 = sub['name']
            superCategoryId = sub['superCategoryId']
            id = sub['id']
            # 拼接三级类目链接
            link3 = link.format(superCategoryId,id)
            print(cate1,cate3,link3)
    pass

get_cate2()