import scrapy
class TengSpider(scrapy.Spider):
    name = 'teng'
    allowed_domains = ['qq.com']
    start_urls = ["https://ke.qq.com/course/list?mt=1001"]

    def parse(self, response):
            # all = response.xpath('//div[@class="course-list"]/div')  # 易错
            # for item in all:
                # name = item.txpath('.//h3[@class="kc-course-card-name"]/@title').extract()[0]
                # link = item.xpath(
                # './/a[@class="kc-course-card js-report-link kc-list-course-card kc-course-card-column"]/@href').exract()[0]
                # class_link = f'https://ke.qq.com{link}'
                # print(class_link, name)

            # pass
            all = response.xpath('//div[@class="course-list"]/div')
            for item in all:
                name = item.xpath('.//h3/@title').extract_first()
                link = item.xpath('.//a/@href').extract_first()
                class_link = f'https://ke.qq.com{link}'
                # 'https://ke.qq.com/course/341933'
                # 'https://ke.qq.com/course/5814785'
                # print(name, class_link)
                # 将数据封装到items中
                item['name'] = name
                item['class_link'] = class_link
                yield item
                
            pass