# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :sql语句.py
%Time       :2022/11/3 14:44
"""
data = {
    'name': '百度',
    'info': '百度，全球大的中文搜索引擎，大的中文网站。',
    'rank':'1'
}
# 插入数据（insert）
inseterStr = 'insert into chin("uname","info","rank")values ("%s","%s","%s");data["info"],data["rank"]'
print(inseterStr)
