# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/12 9:07
# @Author  : xhh
# @Desc    : 简单的验证码识别
# @File    : opencv_captcha.py
# @Software: PyCharm
import cv2 as cv
from PIL import Image
import pytesseract


def recognize_text():
    # 进行灰度处理
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # 进行二值化处理
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # getStructuringElement返回指定形状和结构的元素的尺寸
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 6))
    # 腐蚀运算
    binl = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 1))
    open_out = cv.morphologyEx(binl, cv.MORPH_OPEN, kernel)
    cv.bitwise_not(open_out, open_out)  # 背景变为白色
    cv.imshow("转换", open_out)
    textImage = Image.fromarray(open_out)
    text = pytesseract.image_to_string(textImage)
    print("This OK:%s" % text)


src = cv.imread("../captcha/tupian/3AWM.jpg")
cv.imshow("原来", src)
recognize_text()
cv.waitKey(0)
cv.destroyAllWindows()
