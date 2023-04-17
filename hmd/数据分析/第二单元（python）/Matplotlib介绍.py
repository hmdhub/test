# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :Matplotlib介绍.py
%Time       :2022/11/21 15:52
"""

import matplotlib
from matplotlib import pyplot as plt
print(matplotlib.__version__)
import numpy as np

x = np.arange(-50,51)
y = x ** 2  # y次方
plt.plot(x,y)
plt.show()