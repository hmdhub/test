# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :下午 腾讯课堂.py
%Time       :2022/10/31 15:49
"""
import requests
import json
from lxml import html
import csv
with open("tengxun.csv",'w+',newline='',encoding="utf_8_sig") as f:
        obj = csv.writer(f)
        row = ['课程名字', '课程链接']
        obj.writerow(row)
        for i in range(1,35):
            url = f"https://ke.qq.com/course/list?mt=1001&st=2054&page={i}"
            header = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
            }
            resp = requests.get(url,headers = header)
            #指定编码格式
            resp.encoding = 'utf-8'
            ht = html.etree.HTML(resp.text)
            all = ht.xpath('//div[@class="course-list"]/div')
            for item in all:
                link = item.xpath('.//a[@class="kc-course-card js-report-link kc-list-course-card kc-course-card-column"]/@href')
                name = item.xpath('.//div[@class="kc-course-card-content"]/h3/text()')
                if name and link:
                    name = name[0]
                    link = 'https://ke.qq.com' + link[0]
                    info = [name,link]
                    obj.writerow(info)
                else:
                    name = ''
                    link = ''
                    info = [name,link]
                    obj.writerow(info)



















