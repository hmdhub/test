# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :东方财富 基金网.py
%Time       :2022/10/18 9:19
"""
from selenium import webdriver
from lxml import html
import time
brower = webdriver.Chrome()
#请求网址
brower.get("http://fund.eastmoney.com/data/diyfundranking.html")
info_li = brower.find_elements_by_xpath('//table[@id="dbtable"]/tbody/tr')
for i in range(1,321):
    for item in info_li:
        #序号
        no_li = item.find_element_by_xpath('//table[@id="dbtable"]/tbody/tr/td[2]').text
        # 基金代码
        daima_li = item.find_element_by_xpath('//table[@id="dbtable"]/tbody/tr/td[3]').text
        # 基金简称
        jian_li = item.find_element_by_xpath('//table[@id="dbtable"]/tbody/tr/td[4]').text
        # 基金涨幅
        zhangfu_li = item.find_element_by_xpath('//table[@id="dbtable"]/tbody/tr/td[5]').text
        # print(no_li, daima_li,jian_li,zhangfu_li)

        # 翻页：
        # fanye = self.brower.find_elements_by_xpath('//div[@id="pagebar"]/label')
        #             new = fanye[7].click()
    a = brower.find_elements_by_xpath('//div[@id="pagebar"]/label')
    new = a[7].click()
    time.sleep(2)   #  翻页操作必须休息一下不然会被封
# brower.quit()

