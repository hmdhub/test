# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :Mytengxun.py
%Time       :2022/11/3 14:11
"""
import scrapy
from Mytengxun.items import MytengxunItem

class TengSpider(scrapy.Spider):
    name = 'Mytengxun'
    allowed_domains = ['qq.com']
    start_urls = ["https://ke.qq.com/course/list?mt=1001"]

    def parse(self, response):
        # item = MytengxunItem()
        all = response.xpath('//div[@class="course-list"]/div')
        for it in all:
            item = MytengxunItem()
            name = it.xpath('.//h3/@title').extract_first()
            link = it.xpath('.//a/@href').extract_first()
            class_link = f'https://ke.qq.com{link}'
            # 'https://ke.qq.com/course/341933'
            # 'https://ke.qq.com/course/5814785'
            # print(name, class_link)
            # 将数据封装到items中
            item['name'] = name
            item['class_link'] = class_link
            yield item

        pass