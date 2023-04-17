# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :王者荣耀习题.py
%Time       :2022/10/27 13:36
"""
# 导包
import requests
import json
# import csv
import re
from lxml import html

def get_hero():  # 方法
    # 请求信息
    skin = '//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-tengxun.jpg'
    url = "https://pvp.qq.com/web201605/js/herolist.json"
    header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # 请求网页
    response = requests.get(url,headers = header)
    response.encoding = "gbk"
    a = response.text
    # ht = html.etree.HTML(resp.text)
    print(a)

    # 使用json模块
    info = json.loads(a)
    # info中括号开头要列循环
    for he in info:
        ename = he['ename']
        cname = he['cname']
        img = skin.format(ename,ename)
        'https:// game.gtimg.cn / images / yxzj / img201606 / skin / hero - info / 521 / 521 - bigskin - tengxun.jpg'
        print(ename,cname,img)

pass
#get_hero()
#


def get_hero2():
    url = "https://pvp.qq.com/web201605/herolist.shtml"
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # 请求网页
    response = requests.get(url, headers=header)
    response.encoding = "gbk"
    b = response.text
    # print(b)
    # 转化对象
    page = html.etree.HTML(b)
    # 列表
    hero_lit = page.xpath('//ul[@class="herolist clearfix"]/li')
    # for循环
    for i in hero_lit:
        hero_name = i.xpath('.//img/@alt')[0]
        hero_img = i.xpath('.//img/@src')[0]
        # 拼接img路径
        imgs = 'https:' + hero_img
        'https: // game.gtimg.cn / images / yxzj / img201606 / heroimg / 505 / 505.jpg'
        '// game.gtimg.cn / images / yxzj / img201606 / skin / hero - info /110/110 - bigskin - tengxun.jpg'
        # 小头像
        h = 'https:' + imgs
        # 皮肤
        j = h.replace('/heroimg/','/skin/hero-info/').replace('.jpg','-bigskin-tengxun.jpg')
        print(hero_name,j)

        # print(hero_name, imgs)

    pass
get_hero2()

