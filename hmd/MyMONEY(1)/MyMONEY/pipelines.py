# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from  MyMONEY.optMysql import Sql
class MymoneyPipeline:
    def process_item(self, item, spider):
        try:
            Sql.insert_info(item)
        except Exception as w:
            print(w.args)
        return item
