# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from Wy.write import my
class WyPipeline:
    def process_item(self, item, spider):
        try:
            # my.insert_write(item)
            my.insert_write2(item)
        except  Exception as q:
            print(q.args)
        return item
