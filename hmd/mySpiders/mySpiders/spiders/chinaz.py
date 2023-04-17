import scrapy
import requests

class ChinazSpider(scrapy.Spider):
    name = 'chinaz'  # 爬虫识别的名称
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
            for item in all:
                data = {}
                name = item.xpath('.//h3[@class="rightTxtHead"]/a/@title').extract()[0]
                link = item.xpath('.//h3[@class="rightTxtHead"]/span/text()').extract()[0]
                info = item.xpath('.//p[@class="RtCInfo"]/text()').extract()[0]
                paming = item.xpath('.//div[@class="RtCRateCent"]//strong/text()').extract()[0]
                print(name, link, info, paming)
                data['name'] = name
                data['info'] = info
                data['link'] = link
                # 存储csv文件操作；
                    # 1.使用yield关键词
                    # 2.返回字典格式
                    # 3.运行命令

                 # yield {
                #     '名字': name,
                #     '简介': info,
                #     '排名': link
                # }
                yield data
            pass








  # all = response.xpath('//ul[@class="listCentent"]/li')
            # for item in all:
            #     name = item.xpath('.//a/@title').extract()[0]
            #     info = item.xpath('.//p[@class="RtCInfo"]/text()').extract().extract_first()
            #     rank = item.xpath('.//strong[@class"col-red02"]/text()').extract()[0]
            #     print(name)
            #     print(info)
                # print(type(name))