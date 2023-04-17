# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :博客园 另一种方法.py
%Time       :2022/11/2 11:33
"""
import requests
import csv
from lxml import html

class Hotdog(object):

    def __init__(self):
        self.url = 'https://www.cnblogs.com/'
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
          }

    def cool(self):
        ku = ['https://www.cnblogs.com/sitehome/p/2']
        for i in ku:
            reponse = requests.get(i, headers=self.header)
            reponse.encoding = 'utf-8'
            # print(reponse.text)
            page = html.etree.HTML(reponse.text)
            hot = page.xpath('//div[@id="post_list"]/article')
            for one in hot:
                link = one.xpath('.//a[@class="post-item-title"]/@href')[0]
                name = one.xpath('.//a[@class="post-item-title"]/text()')[0]
                print(link, name)
                # self.write([name, link])

    def write(self, pk):
        with open('pink.csv', 'a+', newline='')as f:
            w = csv.writer(f)
            w.writerow(pk)

uk = Hotdog()
uk.cool()