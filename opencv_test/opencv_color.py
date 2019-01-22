# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/10 11:20
# @Author  : xhh
# @Desc    : 色彩处理
# @File    : opencv_color.py
# @Software: PyCharm
import cv2


# 色彩空间转换
def color_space_demo(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # RGB转换为GRAY，这里的生成的gray图是单通道的
    cv2.imshow('gray', gray)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # RGB转换为hsv
    cv2.imshow('hsv', hsv)
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)  # RGB转换为yuv
    cv2.imshow('yuv', yuv)


src = cv2.imread('../captcha/tupian/ren3.jpg')
cv2.namedWindow(u"原来", cv2.WINDOW_NORMAL)
cv2.imshow(u"原来", src)
color_space_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
