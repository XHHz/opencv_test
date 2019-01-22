# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/11 17:21
# @Author  : xhh
# @Desc    : 图像轮廓发现，并画出图像的轮廓
# @File    : opencv_contours.py
# @Software: PyCharm
import cv2
import numpy as np


def contours(image):
    dst = cv2.GaussianBlur(image, (3, 3), 0)
    # 转化为灰度图像
    gray = cv2.cvtColor(dst, cv2.COLOR_RGB2GRAY)
    # 转换为二值图像
    ret, binary = cv2.threshold(gray, 0, 255,  cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow('binary', binary)
    # findContours用来检测图像的轮廓
    cloneImg, contours, heriachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        # 在原图上画出图像的轮廓
        cv2.drawContours(image, contours, i, (0, 0, 255), 2)
    cv2.imshow("contpurs", image)


src = cv2.imread("../captcha/tupian/example.jpg")
cv2.imshow('def', src)
contours(src)
cv2.waitKey(0)
cv2.destroyAllWindows()



