# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :回顾慧聪网.py
%Time       :2022/10/13 10:40
"""
# 回顾慧聪网
'''''
之前的代码会报错的原因是因为
如果在for循环的时候执行代码会出现替换或者重命名或者可以理解为更改的结果
'''''
# 比如
a = {
    'name' : "贺梦迪"
}
a['name'] = '贺 ' # {'name': '贺'} 最终的结果会被替换掉
print(a)