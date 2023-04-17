# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午：东方财富 基金网.py
%Time       :2022/10/18 9:18
"""
from lxml import html
import time
from selenium import  webdriver
# url = "https://fund.eastmoney.com/"
# header = {
#     "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
# }

brower = webdriver.Chrome()
#请求网址
brower.get('http://fund.eastmoney.com/data/diyfundranking.html')
#获取页面表格里所有的基金行
info_li = brower.find_elements_by_xpath('//table[@id="dbtable"]/tbody/tr')
#遍历得到每一行基金信息
for item in info_li:
# 使用selenium中的xpath取值
    #序号
    no_li= item.find_element_by_xpath('//table[@id="dbtable"]/tbody/tr/td[2]').text
    #基金代码
    daima_li = item.find_element_by_xpath('//table[@id="dbtable"]/tbody/tr/td[3]').text
    #基金简称
    jian_li = item.find_element_by_xpath('//table[@id="dbtable"]/tbody/tr/td[4]').text
    #期间涨幅
    zhang_li = item.find_element_by_xpath('//table[@id="dbtable"]/tbody/tr/td[5]').text
    print(no_li,daima_li,jian_li,zhang_li)
    # zhang_li = item.find_element_by_xpath('//table[@id="dbtable"]/tbody/tr/td[5]')
    # zhang_li.get_attribute('text')
    # print(no_li,daima_li,jian_li,zhang_li)
# 翻页：
ele = brower.find_elements_by_xpath('//div[@id="pagebar"]//label')
#找到下一页按键进行点击操作
ele[7].click()
# 重复第一次取值操作

time.sleep(5)
brower.quit()



