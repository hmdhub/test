""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/10/26 8:41
file :one.PY
"""""
from pymongo import  *
import  requests
from  lxml import  html
class Bao():
    def __init__(self):
        self.header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
        self.url ='http://www.bao66.cn/web/'
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.bao # 第三步写入mongo_db数据库
        self.data = self.db.stu
        self.client.close()
    def info(self): # 第一步
        all = requests.get(self.url,self.header)
        # 状态码
        print(all.status_code)
        # 网页原代码
        print(all.text)
        # 请求的url
        print(all.url)

    def gooods(self):
        for i in range(1,6):  # 0是首页1也是首页 # 实现翻页操作
            url = f'http://www.bao66.cn/search/web,407,钱包,,{i},5.html'
            res = requests.get(url,self.header)
            html1 = html.etree.HTML(res.text)
            all = html1.xpath('//ul[@class="product_box"]/li')
            for b in all:
                dict1={}
                name = b.xpath('.//div[@class="indexbox"]//p/@title')
                if name:
                    dict1["name"]=name[0]
                else:
                    dict1["name"]=''
                title = b.xpath('.//p[@class="code"]/a/text()')
                if title:
                    dict1["title"]=title[0]
                else:
                    dict1["title"] = ''
                price = b.xpath('.//p[@class="desc_hover"]/a/b/text()')
                if price:
                    dict1["price"]=price[0]
                else:
                    dict1["price"]=''
                self.data.insert_one(dict1)
        self.client.close() # 缩进
niu = Bao()   # 实例化一个对象
niu.gooods()#  根据对象调用对应的方法和属性
# niu.info()
