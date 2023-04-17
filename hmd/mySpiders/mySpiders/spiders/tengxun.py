import scrapy
import requests

class TengxunSpider(scrapy.Spider):
    name = 'tengxun'  # 爬虫识别的名称
    allowed_domains = ['tengxun.com']   # 爬取的起始URL元组或列表爬虫搜索的域名名范围
    start_urls = [] # 用方法二时加上
    # 方法一 翻页
    # start_urls = [f'https://ke.qq.com/course/list?mt=1001&st=2064&page={i}' for i in range(1,35)]   #列表推导式

    # 方法二  翻页
    for i in range(1, 35):
        s = 'https://ke.qq.com/course/list?mt=1001&st=2064&page=' + str(i)
        start_urls.append(s)
    #   s = 'https://ke.qq.com/course/list?mt=1001&st=2064&page={i}'
    print(i)


    #'https://ke.qq.com/course/list?mt=1001&st=2064&page={}'] #http://tengxun.cn/
    # start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2064&page=1',
    #               'https://ke.qq.com/course/list?mt=1001&st=2064&page=2',
    #               'https://ke.qq.com/course/list?mt=1001&st=2064&page=3']

    def parse(self, response):
        all = response.xpath('//div[@class="course-list"]/div')
        for item in all:
           data = {}
           name = item.xpath('.//h3/@title').extract_first()
           link = item.xpath('.//a/@href').extract_first()
           link1 = 'https://ke.qq.com'+ link
           print(name, link1)
           if name:
               name = name
           else:
               name = ''
           if link:
               link = link
           else:
               link = ''
           data['name'] = name
           data['link1'] = link1
           cu_url = response.url
           print(cu_url)
           yield data
        pass



