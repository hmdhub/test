# -*- coding��utf-8 -*-
"""
%Author     :hmd
%FileName   :matplotlib����.py
%Time       :2022/11/24 11:04
"""
# import matplotlib
# print(matplotlib.__version__)
from matplotlib import pyplot as plt
import numpy as np


# ���ڴ�1991��2020,30�������
dates = np.arange(1991,2021)
# print(dates)
dates  # ���

# ʹ��numpy�����������
sales = np.random.randint(50,500,size=len(dates))
# sales
print(sales)


# ��������ͼ
# x������ֵ���ͣ�ʹ�õ���Ԫ�ر���int��
plt.xticks([dates[i] for i in range(0,len(dates),2)],rotation=45)
plt.plot(dates,sales)

# �ַ�������
# x ��
dates = np.arange(1991,2021).astype(np.str_) # astype(np.str_)ָ���������ͣ�str_�ַ�����
# y �᣺����
sales = np.random.randint(50,500,size=len(dates))
# ��ͼ
a = [i for i in range(0,len(dates),2)]
print(a)
plt.xticks([i for i in range(0,len(dates),2)],rotation=45)
plt.plot(dates,sales)

"""
�ܽ᣺
    1.x������ֵ�ͣ��ᰴ����ֵ�ͱ�����Ϊx�������
    2.x��Ϊ�ַ������ͣ��ᰴ��������Ϊx�������
"""