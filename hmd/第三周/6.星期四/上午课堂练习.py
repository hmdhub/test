# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午课堂练习.py
%Time       :2022/10/13 13:43
"""
# 加引号 才可以运行
# 把慧聪网的数据导入pymysql 里面
import  pymysql  # 创建游标
# 没有问题无误
import requests
from lxml import html
class Hui(object):
    def __init__(self):
        self.header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
        self.url = 'https://www.hc360.com/'

        # 数据库连接
        self.conn = pymysql.connect(host='localhost',
                               user='root',
                               database='hmd',
                               password='123456',

                             port=3306)

        # 获取游标
        self.cursor=self.conn.cursor()
    #得到类目信息
    def cate(self):
        response = requests.get(self.url,self.header)
        response.encoding = 'utf-8'
        page = html.etree.HTML(response.text)
        #所有类目列表
        cate_li = page.xpath('//dd[@class="aside-dd"]/dl')
        for item in cate_li:
            #一级类目名字
            cate1 = item.xpath('.//dt[@class="sub-menu-dt"]/span/text()')
            #得到二级类目列表
            cate2_li = item.xpath('.//dd[@class="sub-menu-dd"]/dl')
            for i in cate2_li:
                # 二级类目名字
                cate2 = i.xpath('.//dt/text()')[0]
                # 得到三级类目列表
                cate3_li = i.xpath('.//dd/a')
                for j in cate3_li:
                    cate3 = j.xpath('.//text()')[0]
                    cate3_link = j.xpath('.//@href')[0]
                    link = self.url+cate3_link
                    shangpin = self.good(link,cate1,cate2,cate3)
                    if shangpin: # k强转型str类型
                        data = {k: '"'+str(v)+'"' for k,v in shangpin.items()}  #shangpin.items()可以得到每一个values
                        sql = f'insert into hui(name,cate1,cate2,cate3,price,img) values ({data["name"]},{data["cate1"]},{data["cate2"]},{data["cate3"]},{data["price"]},{data["img"]})'  # 小彩里面要有相应的表，（name,cate1,cate2,cate3,price,img 类型为varchar）和 id 是相应的表名
                        print(sql)
                        print('@@@@@@@@@@@@@@@@@@@')
                        self.save(sql)
                    # self.cursor.close()
                    # self.conn.close()
                    # shangpin['cate1'] = cate1
                    # shangpin['cate2'] = cate2
                    # shangpin['cate3'] = cate3 # 原来的代码会出现覆盖的情况
                    # print('111111111111111111111111')

    # 得到商品信息
    def good(self,s,cate1,cate2,cate3):
        response = requests.get(s, headers=self.header)
        response.encoding = 'utf-8'
        # 解析
        info = html.etree.HTML(response.text)
        li_goods = info.xpath('//div[@class="wrap-grid"]/ul/li')
        for item in li_goods:
            good = {} # 每一次的for循环之后都会有一个空字典 就不会出现为空的情况
            name = item.xpath('.//dd[@class="newName"]/a/@title')  # 名字
            if len(name) > 0:
                good['name'] = str(name[0])
            else:
                good['name'] = ''
            price = item.xpath('.//span[@class="seaNewPrice"]/text()')  # 价格
            if len(price) == 2:
                good['price'] = price[1].replace('\r\n', '')
            else:
                good['price'] = 0
            img = item.xpath('.//a[@class="nImgBox title"]/img/@src')
            if len(img) > 0:
                a = img[0].replace('../', 'https://www.hc360.com/')
                good['img'] = a
            else:
                good['img'] = ''
            good["cate1"] = cate1
            good["cate2"] = cate2  # 循环外面
            good["cate3"] = cate3
            return good
# 新加的一个方法，用来将数据插入mysql数据库
    def save(self,sql):
        # tengxun.连接数据库
        # 2.获取游标
        # 执行SQL语句
            self.cursor.execute(sql)
        # 提交数据
            self.conn.commit()
        #conn.close()
# 实例化对象
h = Hui()
# 调用方法
# try:
h.cate()
