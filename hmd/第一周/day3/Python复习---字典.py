# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :Python复习---字典.py
%Time       :2022/10/12 9:54
"""
#  字典的遍历
a = {'姓名': '蔡梦丹', "性别": '女', '爱好': 'run'}
# 循环        循环的方式
for key in a.keys():
    #key:姓名         values:蔡梦丹        我是第一种循环
    ''''
    %-10s:左对齐
    %+10s:右对齐   10表示10个空间
    '''
    print("key:%-10s values:%-10s" % (key,a[key]), "我是第一种循环")  # 姓 名 性 别 爱 好
for key, value in a.items():  # 姓名 蔡梦丹 性别 女 爱好 run
    print(key, value, '我是第二种循环')
for v in a:
    print(v, a[v], '我是第三种循环')
#  创建
b = dict([(1, 'c'), (2, 'b'), (3, 'j')])  # {tengxun: 'c', 2: 'b', 3: 'j'}
print(b)
c = {}  # 创建空字典
print(c)
# 添加 （如果没有会自动创建）
b[4] = "帅哥"
print(b)  # {tengxun: 'c', 2: 'b', 3: 'j', 4: '帅哥'}
# 清空
cc = c.clear()  # None
print(cc)
# 修改
b[2] = 'cmd'
print(b)  # {tengxun: 'c', 2: 'cmd', 3: 'j'}
# 删除
del b[1]  # {2: 'cmd', 3: 'j'}
print(b)
# 更新
aaa = {1111: '美女'}
z = b.update(aaa)
print(b)  # {2: 'cmd', 3: 'j', 1111: '美女'}
# 循环
for key in b.values():
    print(key)  # cmd j  美女
# 查
#  方法一
chart = b[3]  # j 根据键找到对应的值
print(chart)
# 方法二
dd = b.get(1)  # c
print(dd)
print(len(b), b)  # {2: 8, 3: 27, 4: 64, tengxun: tengxun} <class 'dict'>
# 字典的推导式
dic = {
    x:x**3 for x in (2, 3, 4, 1, 2, 1)
}
print(dic,type(dic)) # {2: 4, 3: 9, 4: 16, tengxun: tengxun}
#