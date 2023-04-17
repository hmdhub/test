# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午 英雄联盟.py
%Time       :2022/10/19 8:16
"""
import requests
from lxml import html
import json
import csv
# 请求地址
url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=53"
# 请求地址
header = {
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
# 发送请求
resp = requests.get(url,headers=header)
a = resp.text
all = json.loads(a)
# print(all)

# 网页源码不是HTML数据，不需要xpath解析
# print(resp.text)
# 反序列化------字典
# info = json.loads(a)
# print(type(info))
# print(info)
# 字典取值   列表
# heros = info['hero']
# for hero in heros:
#     heroid = hero['heroId']
#     name = hero['name']
#     alias = hero['alias']
#     print(heros,name,alias)
# 将数据存入csv文件中

for item in all['hero']:
     name = item['name']
     yingwen = item['alias']
     id = item['heroId']
     # print(name,yingwen,id)

# 请求图片地址
     img_link = 'https://game.gtimg.cn/images/lol/act/img/skin/big'
     skin_img = img_link + id + '000.jpg'
#  请求图片链接
     skin_res = requests.get(skin_img,headers=header)
     # 将图片写入本地    ----------对于图片和视频 （二进制）
     with open(f'img/{name}.jpg','ab')as pictuer:
        pictuer.write(skin_res.content)
        pass
     # for k in range(10):
     #    result_url = img_link + id  + '%03d' % k + '.jpg'  # '%03d'%k[000到009]'
     #    # if k <=9:
     #    #     s = '00'+str(k)
     #    # else:
     #    #     s = '0'+str(k)
     #    # 3.保存图片
     #    img = requests.get(result_url)
     #    if img.status_code == 200:
     #        with open('img/%s%d.jpg' % (yingwen,k),'wb')as f:
     #            # img.content 就是写入图片的二进制数据
     #            f.write(img.content)










     # 将数据写入csv文件中
with open('lol.csv','a+',encoding='UTF-8',newline='') as f:
     spolid = csv.writer(f)
     spolid.writerow(['英雄id','英雄名字','英文名字'])
     for item in all['hero']:
         title = item['name']
         yingwen = item['alias']
         id = item['title']
         # 转化为列表
         ss = [title, id ,yingwen]
         # 写入csv
         spolid.writerow(ss)
#          print(title, yingwen, id)
# print("写入完毕！")

#  自己拼接路由看皮肤图片怎么获取

# with open("stu.csv",'a') as f:
#    row3 = ['英雄', '英文', '地址']
#
# #     #写入
# #     # w = csv.writer(f)
# #     # w.writerow(row3)
#    write=csv.writer(f)
#    write.writerow(row3)
# print("写入完毕！")














