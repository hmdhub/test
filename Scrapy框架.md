### Scrapy框架

#### 介绍

```
Scrapy 是一个基于 Twisted实现的专业的、高效的异步处理爬虫框架，Scrapy 框架用纯Python实现。

Twisted：一个采用 Python 实现的基于事件驱动的网络引擎框架，用 Twisted 来处理网络通讯可以加快我们的下载速度，不用自己去实现异步框架。

Scrapy 框架用途非常广泛，可以提取网站数据、网络监测以及自动化测试等，Scrapy 也可以根据自己需求所需要的数据进行定制。

Scrapy 框架使用 lxml（专业的 XML 处理包）、cssselect 高效地提取 HTML 页面的有效信息，同时它也提供了有效的线程管理。

Scrapy 框架使用起来也很方便，开发人员只需要定制开发几个模块就可以实现一个爬虫程序，用来抓取网页数据或图片。

```

![1665926892030](C:\Users\AA\AppData\Roaming\Typora\typora-user-images\1665926892030.png)

#### scrapy组件

课本（p179）

```
Engine，引擎，是整个框架的核心，负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等

Scheduler， 调度器，用来接受引擎发过来的Request请求并按照一定的方式加入队列中，并在引擎再次请求的时候提供给引擎。

Downloader，下载器，用于下载Engine请求到的网页内容，并将其获取到的Responses交还给Engine(引擎)，由Engine交给Spider来处理。

Spiders，爬虫，其内定义了爬取的逻辑和网页的提取数据规则，它主要负责处理所有Responses并生成提取结果，并将新的URL提交给引擎，再次进入Scheduler(调度器)。   提取的结果有两种：1.想要的数据（Item） 2.url

Item Pipeline，项目管道，负责处理Spider中获取到的Item，并进行进行清洗、验证和存储数据。

Downloader Middlewares，下载器中间件，自定义扩展下载功能的组件，位于引擎和下载器之间的钩子框架，主要是处理引擎与下载器之间的请求及响应。

Spider Middlewares， 蜘蛛中间件，位于引擎和蜘蛛之间的钩子框架，可以自定扩展和操作引擎和Spider中间通信的功能组件。
```

```
scrapy框架有哪几个组件/模块？简单说一下工作流程。
Scrapy Engine: 这是引擎，负责Spiders、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等等！（像不像人的身体？）
Scheduler(调度器): 它负责接受引擎发送过来的requests请求，并按照一定的方式进行整理排列，入队、并等待Scrapy Engine(引擎)来请求时，交给引擎。
Downloader（下载器）：负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spiders来处理，
Spiders：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)，------------两种结果：1.url  2:item我们想要的数据
Item Pipeline：它负责处理Spiders中获取到的Item，并进行处理，比如去重，持久化存储（存数据库，写入文件，总之就是保存数据用的）
Downloader Middlewares（下载中间件）：你可以当作是一个可以自定义扩展下载功能的组件
Spider Middlewares（Spider中间件）：你可以理解为是一个可以自定扩展和操作引擎和Spiders中间‘通信‘的功能组件（比如进入Spiders的Responses;和从Spiders出去的Requests）

```

工作流程

```
数据在整个Scrapy的流向：
程序运行的时候，
引擎：Hi！Spider, 你要处理哪一个网站？
Spiders：我要处理百度（www.baidui.com）
引擎：你把第一个需要的处理的URL给我吧。
Spiders：给你第一个URL是XXXXXXX.com
引擎：Hi！调度器，我这有request你帮我排序入队一下。
调度器：好的，正在处理你等一下。
引擎：Hi！调度器，把你处理好的request给我，
调度器：给你，这是我处理好的request
引擎：Hi！下载器，你按照下载中间件的设置帮我下载一下这个request
下载器：好的！给你，这是下载好的东西。（如果失败：不好意思，这个request下载失败，然后引擎告诉调度器，这个request下载失败了，你记录一下，我们待会儿再下载。）
引擎：Hi！Spiders，这是下载好的东西，并且已经按照Spider中间件处理过了，你处理一下（注意！这儿responses默认是交给def parse这个函数处理的）
Spiders：（处理完毕数据之后对于需要跟进的URL），Hi！引擎，这是我需要跟进的URL，将它的responses交给函数 def  xxxx(self, responses)处理。还有这是我获取到的Item。
引擎：Hi ！Item Pipeline 我这儿有个item你帮我处理一下！调度器！这是我需要的URL你帮我处理下。然后从第四步开始循环，直到获取到你需要的信息，
注意！只有当调度器中不存在任何request了，整个程序才会停止，（也就是说，对于下载失败的ＵＲＬ，Scrapy会重新下载。）
以上就是Scrapy整个流程了。
```



#### 安装

```
pip版本设置：python -m pip install pip==20.2.4
pip install scrapy
pip22.3需要python3.9版本

问题1.error: can't find Rust compiler
	  	Non-zero exit code (2)
解决：指定pip版本

问题2：mportError: No module named w3lib.http
解决：pip install w3lib

问题3：ImportError: No module named twisted
解决：pip install twisted

问题：4ImportError: No module named lxml.HTML
解决：pip install lxml
问题5：error: libxml/xmlversion.h: No such file or directory
解决：apt-get install libxml2-dev libxslt-dev
	 apt-get install Python-lxml

问题6：ImportError: No module named cssselect
解决：pip install cssselect

问题7：ImportError: No module named OpenSSL
解决：pip install pyOpenSSL
问题8：缺少Microsoft Visual C++ 14.0组件
	访问提示地址，下载安装一直下一步，不需要更改（安装后需要重启）
	安装中如果出现错误 ，下载安装.NET Framework 4.5.1 或以上版本or 
问题9：Twisted安装错误（fatal error c1083 'basetsd.h' No such file）
	解决：下载 twisted (https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)
		  安装 pip install 带扩展名的完整文件名（.whl）
```

#### 爬虫步骤

##### 新建项目

```
scrapy startproject + 项目名
eg: scrapy startproject mySpider 即是创建一个项目名为mySpider的项目
打开终端，进入自定义的项目目录（例如，在Windows系统下的“D:\PythonProject”目录），运行如下命令 scrapy startproject mySpider
```

```
目录文件介绍：
 scrapy.cfg --配置文件，用于存储项目的配置信息。
 mySpider/  --项目的Python模块，将会从这里引用代码。
 mySpider/items.py --实体文件，用于定义项目的目标实体（实体数据）。
 mySpider/middlewares.py --中间件文件，用于定义Spider中间件。
 mySpider/pipelines.py --管道文件，用于定义项目使用的管道。
 mySpider/settings.py --设置文件，用于存储项目的设置信息。
 mySpider/spiders/ --存储爬虫代码的目录。
```

##### 明确目标

```
目标：站长之家，抓取内容就是页面中所有站点的名字、排名和网站简介等数据。
https://top.chinaz.com/hangye/ 行业排行
```

![1666161565108](C:\Users\AA\AppData\Roaming\Typora\typora-user-images\1666161565108.png)

```
Scrapy提供了基类scrapy.Item用来表示实体数据。我们一般需要创建一个继承自scrapy.Item的子类，并为该子类添加scrapy.Field类的属性来表示实体数据。

import scrapy
class MyspiderItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()

```

##### 制作爬虫

使用Scrapy框架制作爬虫的第三步就是制作Spiders，也就是负责爬取和提取数据的爬虫。我们把制作Spiders分为三个步骤实现，分别是：创建爬虫、运行爬虫、提取数据

###### 创建爬虫

首先要在项目中创建一个爬虫，创建爬虫的命令格式如下：
scrapy genspider 爬虫名称 "爬取域"

```
打开终端，来到当前目录的子目录mySpider/spiders，使用创建爬虫的命令创建一个名为chinaz的爬虫，并指定爬取域的范围为“chinaz.com”，具体如下。
scrapy genspider chinaz " chinaz.com "
```

执行后spiders文件夹中会生成py文件

![1666162307052](C:\Users\AA\AppData\Roaming\Typora\typora-user-images\1666162307052.png)



```
 Spider -- 爬虫基类。
 name -- 爬虫的识别名称。
 allow_domains -- 爬虫搜索的域名范围。
 start_urls -- 爬取的起始URL元组或列表。 eg:分页start_urls = ['https://zz.esf.fang.com/house/i3%d/'%i for i in range(1,100)]
 parse方法 -- 用于解析网络响应
```

###### 提取数据

我们已经成功爬取到了网页的源码。要想提取数据，需要先观察页面源码，定位目标数据，分析和了解目标数据的展示结构

使用xpath提取数据

```python
    def parse(self, response):
        info = response.xpath('//ul[@class="listCentent"]/li')
        for ite in info:
            # response.xpath()得到的数据类型<class 'scrapy.selector.unified.SelectorList'>
            # extract()返回列表  extract_first()返回列表值[就是取第一个]
            name = ite.xpath('.//h3[@class="rightTxtHead"]/a/text()').extract_first()  # 名称
            info = ite.xpath('.//p[@class="RtCInfo"]/text()').extract_first()  # 简介
            rank = ite.xpath('.//strong[@class="col-red02"]/text()').extract_first()  # 排名

            print(name,info,rank)
        

```

```python
    def parse(self, response):
        #response是我们的响应

        # 将得到的数据封装到一个MyspiderItem 对象
        items = MyspiderItem()
        # 1.使用xpath解析拿到想要的数据 ，之前确定的3个字段
        # extract()返回列表  extract_first()返回列表值
        # response.xpath()得到的数据类型<class 'scrapy.selector.unified.SelectorList'>
        res = response.xpath('//title/text()').extract()
        items['res'] = res
        yield {
            items
         }
        pass
```

###### 运行爬虫

setthing 文件注释到robots协议

运行爬虫的命令格式为：scrapy crawl 爬虫名称 （需要在spiders目录下运行）

或者 scrapy runspider 文件名.py

```
在项目下新建start.py文件(位置与scrapy.cfg --配置文件 同级)
from scrapy import cmdline
# 运行爬虫
cmdline.execute('scrapy crawl chinaz'.split())
```

###### 

###### 存储数据

**存储文件**

```
存储方式：
运行爬虫的命令后使用 -o选项可以输出指定格式文件
json格式
scrapy crawl chinaz -o data.json
csv格式
scrapy crawl chinaz -o data.csv
FEED_EXPORT_ENCODING = 'utf-8-sig'  # 解决csv文件乱码问题(settings配置)
写文件必须有yield

```

**存储数据库**

1.修改setting文件

​	a. 添加mysql数据库信息

​	b. ITEM_PIPELINES 取消注释

```
Mysql_host = '127.0.0.1'
Mysql_user = 'root'
Mysql_db = 'test'
Mysql_pwd = '123456'
```

2.添加py文件，用来操作数据库

```python
import pymysql
from mySpider import settings
#建立mysql连接
sqlConnect = pymysql.connect(
    host= settings.Mysql_host,
    user = settings.Mysql_user,
    passwd= settings.Mysql_pwd,
    db = settings.Mysql_db
)
#游标
cur = sqlConnect.cursor()
class Sql():
    @classmethod
    def create_db(cls):
        str = 'CREATE TABLE chinaz(id int auto_increment PRIMARY KEY,name VARCHAR(255),info VARCHAR(255),no VARCHAR(255))'
        #执行创建语句
        cur.execute(str)

    @staticmethod
    def inster_chinaz(data):
        insterStr = 'insert into chinaz(name,info,no) values ("%s","%s","%s")' % (
        data['name'], data['info'], data['no'])
        cur.execute(insterStr)  # 执行插入语句
        sqlConnect.commit()  # 提交数据
        pass

    @staticmethod
    def closeMysql():
        cur.close()  # 关闭游标
        sqlConnect.close()  # 关闭连接
        pass

    pass
```

3.修改pipelines.py文件

```python
from mySpider.optmysql import Sql

class MyspiderPipeline:
    def process_item(self, item, spider):
        try :
            # Sql.create_db()
            Sql.inster_chinaz(item)
            pass
        except Exception as ex:
            print(ex.args)
        return item
    def close_spider(self):
        Sql.closeMysql()
```



#### 总结scrapy常用命令

```
创建项目
scrapy startproject + 项目名
创建爬虫
scrapy genspider 爬虫名称 "爬取域"
运行爬虫
scrapy crawl 爬虫名称
保存数据
scrapy crawl 爬虫名称 -o 文件格式
```



#### 扩展

##### scrapy.Spider类中提供了如下一些主要的方法。

| **方法名称**     | **具体说明**                                             |
| ---------------- | -------------------------------------------------------- |
| **init()**       | 初始化方法，负责初始化爬虫名称和start_urls列表           |
| start_requests() | 负责生成Requests对象，交给Scrapy下载并返回response       |
| parse(response)  | 负责解析response，并返回Item或Requests（需指定回调函数） |
| log(message)     | 负责发送日志信息                                         |

##### 中间件添加请求头信息

```python
from scrapy import signals
from faker import Faker
import random

class HeaderClass():
    '''
    设置请求头
    '''
    @staticmethod
    def build_agent():
        user_agent = []
        f = Faker()
        for i in range(15):
            user_agent.append(f.user_agent())
        return user_agent
        pass
    
```

```
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
       
        # 添加请求的头信息
        userAgent = random.choice(HeaderClass.build_agent())
        request.headers.setdefault('User-Agent',userAgent)
        print('========header成功设置')
```

```
关键词
```

##### 案例：

​	存储文件:房天下

​	使用分页:cnblog

​	存储数据库 :cnblog

##### yield关键词

```
def get_yield():
    for i in range(5):
        yield  i

def get_print():
    for i in range(5):
        print(i)
def get_return():
    res = [i for i in range(5)]
    return res


print('yield.....')
c = get_yield() # 调用包含yield，返回生成器队象
print(next(c))  #调用一次返回一个值
print(next(c))
print('print.....')
get_print()
print('return.....')
r = get_return()
for i in r:
    print(i)
```



#### **** 