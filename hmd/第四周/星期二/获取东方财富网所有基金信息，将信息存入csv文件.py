# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :获取东方财富网所有基金信息，将信息存入csv文件.py
%Time       :2022/10/18 17:00
"""
from selenium import webdriver
from lxml import html
import csv
import time
class Mall():
    def __init__(self):
        self.brower = webdriver.Chrome()
        # 请求网址使用自动化
        self.brower.get('http://fund.eastmoney.com/data/diyfundranking.html')
    def write(self):
        with open('news.csv', mode='a+', encoding='utf-8-sig',newline='') as ww:
            title = ['基金代码', '基金简称', '期间涨幅', '期间分红', '分红次数', '起始日期', "单位净值", "累计净值", "终止日期", "单位净值", "累计净值",
                     "成立日期"]
            aa = csv.writer(ww)
            aa.writerow(title)
            for i in range(320):
                all = self.brower.find_elements_by_xpath('//table[@id="dbtable"]//tbody/tr')# 每一列是不一样的
                for item in all:
                    id = item.find_element_by_xpath('.//td[2]').text
                    jjdm = item.find_element_by_xpath('.//td[3]').text
                    jjjc = item.find_element_by_xpath('.//td[4]').text
                    qjzf = item.find_element_by_xpath('.//td[5]').text
                    qjfh = item.find_element_by_xpath('.//td[6]').text
                    fhcs = item.find_element_by_xpath('.//td[7]').text
                    qsrq = item.find_element_by_xpath('.//td[8]').text
                    dwjz = item.find_element_by_xpath('.//td[9]').text
                    ljjz = item.find_element_by_xpath('.//td[10]').text
                    clrq = item.find_element_by_xpath('.//td[11]').text
                    sxf = item.find_element_by_xpath('.//td[12]').text
                    body = [id, jjdm, jjjc, qjzf, qjfh, fhcs, qsrq, dwjz, ljjz, clrq, sxf]
                    aa.writerow(body)
                fanye = self.brower.find_elements_by_xpath('//div[@id="pagebar"]/label')
                new = fanye[7].click()
                time.sleep(1)  #  翻页操作必须休息一下不然会被封
    def gb(self):
        self.brower.quit()
shuju = Mall()
shuju.write()
# shuju.fanye()
shuju.gb()
