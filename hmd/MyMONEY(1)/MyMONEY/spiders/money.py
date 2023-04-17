import scrapy
import json
import  re
from  MyMONEY.items import  MymoneyItem
class MoneySpider(scrapy.Spider):
    name = 'money'
    allowed_domains = ['fund.eastmoney.com/']
    start_urls = ['http://fund.eastmoney.com/data/rankhandler.aspx?op=dy&dt=kf&ft=all&rs=&gs=0&sc=qjzf&st=desc&sd=2021-10-23&ed=2022-10-23&es=0&qdii=&pi=1&pn=50&dx=0&v=0.8509423369157292']
    def parse(self, response):
        # 处理数据 使用正则去解析数据
        info = re.findall('var rankData = (.*)],allRecords:',response.text)
        # print(info)
        new_info= info[0].replace('datas','"datas"').replace('4-08,,,,,,"','4-08,,,,,,"]}')
        # # 序列化取数据
        # print(new_info)
        new_data=json.loads(new_info)
        # print(new_data)
        infomation = new_data['datas']
        # print(infomation)
        for it in infomation:
            item = MymoneyItem()
            # item  = {}
            jjit = it.split(',')[0]
            name = it.split(',')[1]
            qjzf = it.split(',')[3] 
            qjfh = it.split(',')[4]
            twice = it.split(',')[5]
            date = it.split(',')[6]
            jz = it.split(',')[7]
            ljjz1c = it.split(',')[8]
            endtime = it.split(',')[9]
            dwjz = it.split(',')[10]
            ljjz = it.split(',')[11]
            bejintime=it.split(',')[12]
            shouxufei=it.split(',')[13]
            item["jjit"] = jjit
            item["name"] =name
            item["qjzf"] = qjzf
            item["qjfh"] = qjfh
            item["twice"] = twice
            item["date"] =date
            item["jz"] =jz
            item["ljjz1c"] =ljjz1c
            item["endtime"] =endtime
            item["dwjz"] =dwjz
            item["ljjz"] = ljjz
            item["bejintime"] =bejintime
            item["shouxufei"] =shouxufei
            yield  item
        pass
