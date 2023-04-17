""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/19 11:32
file :etst.PY
"""""
# 基本 数据类型
a = '我是梦丹'
b = 2.3
c = 2
d = True
f = 2-2j
print(f)
print(type(a),type(b),type(c),type(d),type(f))
# ---------------------------******************************************
# list
q = [1,2,34,45,67,1222,90]
# 排序
ss = sorted(q)
print(ss,"默认从小到大排序")
# 增
w = q.append(9999)
print(w)
# #  删除
e = q.pop()
print(e,"默认删除最后一个")
# 改
q[2]="33"
print(q,"改变原来的列表数据")
#查
qqq = q[3]
print(qqq)
# 反转
q.reverse()
print(q.reverse(),'我是反转之后的')
# 循环
for i in q:
    print(i)
# 推导式
t = [i for i in q]
print(t,"列表推导式")
# 长度
o = len(q)
print(o,"列表长度",q)
# 排序
qq = [112,3333333,442,443,1,0,5,0]
list2 = sorted(qq,reverse=True) # 降序
print(list2,"降序")
# 切片
qi = qq[1:]
print(qi,"我是切片")
print(qq.sort())  # 为none 没有返回值 # 默认升序
print(qq.reverse())# None全部元素逆置保存
