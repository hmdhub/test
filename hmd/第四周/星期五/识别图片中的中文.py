# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :识别图片中的中文.py
%Time       :2022/10/24 9:35
"""
import pytesseract
from PIL import Image

# 打开图片实例化图片
# 识别中文lang="chi_tra"（简体中文）chi_tra（繁体）
# img = Image.open('gushi.png')
img = Image.open('24.png')
text = pytesseract.image_to_string(img,lang="chi_tra")
print(text)