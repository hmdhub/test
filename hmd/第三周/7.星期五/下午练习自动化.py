# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :下午练习自动化.py
%Time       :2022/10/15 12:24
"""
# 导包
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
from lxml import html
# 如果启动不了浏览器：tengxun.版本不匹配 2.找不到路径（）
bro = webdriver.Chrome()# (executable_path='放路径E:\my_env\yy\Scripts'chromedriver的路径)
bro.get('https://www.baidu.com')
# bro.find_element_by_id('kw').send_keys(u'python')  # u 表示防止中文乱码
# bro.find_element_by_xpath('//input[@id="kw"]').send_keys(u'动物图片')
bro.find_element_by_id('su').send_keys(Keys.ENTER)

# 百度首页
# title = bro.find_element_by_xpath('//title')
# a = title.get_attribute('text') #得到文本信息
# va = bro.find_element_by_xpath('//input[@id="su"]')
# b = va.get_attribute('value')
# print(b)
time.sleep(8)

# 输出网页内容
print(bro.page_source)
# 元素获取
# page = html.etree.HTML(bro.page_source)
# a = page.xpath('//title/text()')
# print(a)



# bro.find_element_by_id('kw').clear() # 清除python
# bro.find_element_by_id('kw').send_keys('河南')
# time.sleep(5)

#bro.find_element_by_id('su').click()  # 相当于浏览器中的百度一下
#time.sleep(3)


# 用完之后记得关闭浏览器，两种方式任选其一（bro.close  bro.quit)
bro.close ()

# 输出网页内容
# print(bro.page_source)  # str response.text

# 浏览器窗口前进和后退
# bro.back() # 后退
# bro.forward() # 前进

# 浏览器最大化
# bro.maximize_window()

# 浏览器最小化
# bro.minimize_window()

# 浏览器设置窗口大小
# bro.set_window_size(480,800) # 宽480 高800

#  无界面的启动方式
# chrome_options = webdriver.ChromeOptions() # ChromeOptions 对象
#  使用headless无界面浏览器模式
# chrome_options.add_argument('--headless')  # 增加无界面选项
# chrome_options.add_argument('--disable-gpu') # 如果不加这个选项，有时定位会出现问题
#
#  启动浏览器，获取网页源代码
# browser = webdriver.Chrome(chrome_options=chrome_options)
# mainUrl = "https://www.baidu.com/"
# browser.get(mainUrl)
# print(browser.page_source)
# browser.quit()
# # bro.quit()


# 模拟下拉操作
obj = webdriver.Chrome()
obj.get('https://news.qq.com/')
info = obj.page_source
# print(info)
# 滚动条
obj.execute_script('window.scrollTo(0,document.body.scrollHeight)')

time.sleep(8)
obj.quit()
