# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from Weibo.hotmysql import Mon

class WeiboPipeline:
    def process_item(self, item, spider):
        try:
            Mon.insert2(item)
            # print(item)
#             print(item) # {'link': 'https://s.weibo.com/weibo?q=%23%E5%B0%8F%E7%9F%AD%E8%85%BF%E4%B9%9F%E8%A6%81%E8%87%AA%E5%BC%BA%E4%B8%8D%E6%81%AF%23&topic_ad=
# ',
# # 'name': '小短腿也要自强不息'}

        except Exception as q:
            print(q.args)

        return item
