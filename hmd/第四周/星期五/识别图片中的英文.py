# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :识别图片中的英文.py
%Time       :2022/10/24 9:20
"""
# 导包
import pytesseract
from PIL import Image
# 打开图片，获取图片的实例化
img = Image.open('tengxun.png')

# 提取图片里的信息

# lang默认为英文（lang='eng'）
text = pytesseract.image_to_string(img,lang='eng')
print(text)