# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :下午课堂笔记  慧聪数据库.py
%Time       :2022/10/13 10:38
"""
 # 所有三级类目下面的商品信息 Teacher
import requests
from lxml import html
class Hui(object):
    def __init__(self):  # 初始化方法  创建对象
        self.url = 'https://www.hc360.com/'
        self.header = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 104.0.0.0Safari / 537.36'
        }

    # 得到类目信息
    def cate(self):
        response = requests.get(self.url, self.header)
        response.encoding = 'utf-8'
        page = html.etree.HTML(response.text)
        # 所有类目列表
        cate_li = page.xpath('//dd[@class="aside-dd"]/dl')  # 找到12个目标目录
        for q in cate_li:
            # print(q)
            # 找到一级目录
            cate1 = q.xpath('.//dt/span/text()')  # 得到一级目录
            # if len(one) ==2:
            # 得到二级目录
            cate2_li = q.xpath('.//dd[@class ="sub-menu-dd"]/dl')
            for b in cate2_li:
                cate2 = b.xpath('.//dt/text()')[0]  # 得到二级类目的值  ok
                cate3_list = b.xpath('.//dd')
                for i in cate3_list:
                    cate3 = i.xpath('./a/text()')[0]
                    cate3_link = i.xpath('.//@href')[0]
                    link = self.url + cate3_link
                    shangpin = self.goods(link, cate1, cate2, cate3)
                    # shangpin['one'] = one
                    # shangpin['two'] = two
                    # shangpin['three'] = three
                    print(shangpin)

    # 得到商品信息
    def goods(self, s, cate1, cate2, cate3):
        responce = requests.get(s, headers=self.header)
        responce.encoding = 'utf-8'
        # 解析
        info = html.etree.HTML(responce.text)
        li_goods = info.xpath('//div[@class="wrap-grid"]/ul/li')  # 找到所有的内容
        # 添加判断
        for item in li_goods:
            dict = {}
            name = item.xpath('.//dd[@class="newName"]/a/@title')  # 看看是否是这个
            # 所有的名字
            if len(name) > 0:
                dict['name'] = str(name[0])
            else:
                dict['name'] = ' '

            price = item.xpath('.//span[@class="seaNewPrice"]/text()')  # 价格 判断有的是没有价格的
            if len(price) == 2:
                dict['newprice'] = price[1].replace('\r\n', '')
            else:
                dict['price'] = 0
            pictures = item.xpath('.//div[@class="picmid pRel"]//img/@src')
            if len(pictures) > 0:
                domin = 'https://www.hc360.com/'
                pictures = item.xpath('.//div[@class="picmid pRel"]//img/@src')
                a = pictures[0].replace("../", domin)
                dict['img'] = a
            else:
                dict['img'] = ' '
            dict['one'] = cate1
            dict['two'] = cate2
            dict['three'] = cate3
            return dict


# 创建对象
h = Hui()
# 调用方法
# try:
h.cate()
# except:
# print('有问题')


