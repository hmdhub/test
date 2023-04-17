# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :识别图片后的数字.py
%Time       :2022/10/24 9:44
"""
import pytesseract
from PIL import Image
# 打开图片，获取图片的实例化
img = Image.open('4.png')
text = pytesseract.image_to_string(img,config='--psm 10--0em 3 -c tessedit_char_whitelist=0123456789')
# config='--psm 10--0em 3 -c tessedit_char_whitelist=0123456789'高版本
# config=‘-psm 7 -c tessedit_char_whitelist=1234567890 低版本
print(text)