# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :matplotlib讲解.py
%Time       :2022/11/24 11:04
"""
# import matplotlib
# print(matplotlib.__version__)
from matplotlib import pyplot as plt
import numpy as np


# 日期从1991到2020,30年的日期
dates = np.arange(1991,2021)
# print(dates)
dates  # 输出

# 使用numpy随机生成销量
sales = np.random.randint(50,500,size=len(dates))
# sales
print(sales)


# 绘制销量图
# x轴是数值类型，使用的是元素本身（int）
plt.xticks([dates[i] for i in range(0,len(dates),2)],rotation=45)
plt.plot(dates,sales)

# 字符串类型
# x 轴
dates = np.arange(1991,2021).astype(np.str_) # astype(np.str_)指定数据类型（str_字符串）
# y 轴：销量
sales = np.random.randint(50,500,size=len(dates))
# 绘图
a = [i for i in range(0,len(dates),2)]
print(a)
plt.xticks([i for i in range(0,len(dates),2)],rotation=45)
plt.plot(dates,sales)

"""
总结：
    1.x轴是数值型，会按照数值型本身作为x轴的坐标
    2.x轴为字符串类型，会按照索引作为x轴的坐标
"""