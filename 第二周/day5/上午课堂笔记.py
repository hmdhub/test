""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/30 9:45
file :上午课堂笔记.PY
"""""
import  requests
from  lxml import  html
url = 'https://www.jd.com'
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=header)
resp.encoding = 'utf-8'
# print(resp.text)
html = html.etree.HTML(resp.text)
data = html.xpath('//li[@ class="cate_menu_item"]/a/text()')
print(data)