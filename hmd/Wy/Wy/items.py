# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cate1_name = scrapy.Field()
    cate2_name = scrapy.Field()
    cate3_name = scrapy.Field()
    # cate3_link = scrapy.Field()
    pass
