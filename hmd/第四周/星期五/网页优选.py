# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :网页优选.py
%Time       :2022/10/24 9:53
"""
import  csv
import  re
import json
import  requests
from lxml import  html
url= 'https://you.163.com/item/list?categoryId=1005002&_stat_area=nav_5&_stat_referer=index'
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=header)
resp.encoding='utf-8'
a =resp.text
# 正则匹配或者字符串分割均可   获取自己想要的数据然后找到自己想要的加上即可
new_a = a.split('var json_Data=')[1].split('</script>')[0]

all_a = new_a.split('json_Data.')[0].replace('}]};','}]}')
# 处理json 数据
aa =json.loads(all_a)
print(aa)
# 处理数据
# info = aa['categoryItemList']
# with open('网页优选.csv','w+',newline='')as all:
#     biaoti = csv.writer(all)
#     da = ['商品名称','商品图片','商品解读']
#     biaoti.writerow(da)
#     for item in info:
#         name =item['itemList']
#         for i in name:
#             new_name = i['name']
#             title  =i['simpleDesc']
#             pic = i['listPicUrl']
#             data = [new_name,pic,title]
#             biaoti.writerow(data)

            # print(new_name,pic,title)
            # print(namew)
        # price=
        # title =
        # img =