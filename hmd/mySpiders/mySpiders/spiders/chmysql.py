# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :chmysql.py
%Time       :2022/11/3 11:25
"""
import scrapy

# 存储数据到mysql数据库
# 1.写spiders文件（该文件要和items文件关联）
# 2.要修改settings文件（添加数据库的配置，打开管道）
# 3.修改管道文件（pipelines文件，该文件可以操作数据库）
# 4.先增加一个py(optMysql)文件用于做增加改查


from mySpiders.items import  MyspidersItem

class ChinazSpider(scrapy.Spider):
    name = 'chmysql'  # 爬虫识别的名称
    allowed_domains = ['chinaz.com']  # 爬取的起始URL元组或列表爬虫搜索的域名名范围
    start_urls = ['http://top.chinaz.com/hangye/']  #

    def parse(self, response):
            # 解析数据  直接用response.xpath（）
            # 和之前的区别：tengxun.不需要进行requests请求（下载器已经做过了）
            # 2.不需要转化文档树对象(内部已经实现)
            # 使用xpath获取数据类型：< class 'scrapy.selector.unified.SelectorList'>
# extract()  使用此方法获取数据（数据类型是列表）
            # 列表取值 ：[0]  或者extract_first()
            all = response.xpath('//ul[@class="listCentent"]/li')
            for it in all:
                # 将数据封装到items中
                item= MyspidersItem()
                # data = {}
                name = it.xpath('.//h3[@class="rightTxtHead"]/a/@title').extract()[0]
                rank = it.xpath('.//h3[@class="rightTxtHead"]/span/text()').extract()[0]
                info = it.xpath('.//p[@class="RtCInfo"]/text()').extract()[0]
                # paming = it.xpath('.//div[@class="RtCRateCent"]//strong/text()').extract()[0]
                
                # 将数据封装到items中
                item['name'] = name
                item['info'] = info
                item['rank'] = rank
                # item['paming'] = paming
                yield item
                # print(name, link, info, paming)
                # data['name'] = name
                # data['info'] = info
                # data['link'] = link
                # 存储csv文件操作；
                    # 1.使用yield关键词
                    # 2.返回字典格式
                    # 3.运行命令

                 # yield {
                #     '名字': name,
                #     '简介': info,
                #     '排名': link
                # }
                # yield data
            pass



