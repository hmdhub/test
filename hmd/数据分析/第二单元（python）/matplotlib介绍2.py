# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :matplotlib介绍2.py
%Time       :2022/11/23 9:55
"""

import matplotlib
from matplotlib import pyplot as plt
print(matplotlib.__version__)
import numpy as np
"""
一.绘制曲线图，要求如下：
        1.显示图形名称
        2.为x轴和y轴定义说明信息
        3.使用中文显示

二.已知数据为2000年到2020年20年之间的销售情况
   sales = [109,150,172,260,273,333,347,393,402,446,466,481,499,504,513,563,815,900,930,961]要求：
   1.绘制年度销量线形图x轴为年份y轴为销量
   2.显示图例
"""
import matplotlib
from matplotlib import pyplot as plt
print(matplotlib.__version__)
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.rcParams['axes.unicode_minus'] = False  # 使负数展现出来
# 年份
times = np.arange(2000, 2020).astype(np.str_)
# 销量
sales = [109, 150, 172, 260, 273, 333, 347, 393, 402, 446, 466, 481, 499, 504, 513, 563, 815, 900, 930, 961]
# plt.title('年销量图', fontsize=20)
plt.title('年销量图',fontsize=20)
# 绘图
# 设置x轴
plt.xlabel('日期', fontsize=10)
plt.ylabel('销量', fontsize=10)
plt.xticks(range(len(times)), rotation=45)
plt.plot(times, sales, label='年销量')
plt.legend(loc='upper right')
for x, y in zip(times, sales):
    plt.text(x, y, '%s个' % y)


