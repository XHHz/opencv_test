# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/12 9:16
# @Author  : xhh
# @Desc    : 对象测量
# @File    : opencv_measure.py
# @Software: PyCharm
import cv2 as cv
import numpy as np


def measure_object(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary img", binary)
    # findContours用来查找检测的轮廓，其中的参数必须是二值图，要先转成灰度图，在转成二值图
    outImg, contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        # 轮廓面积
        area = cv.contourArea(contour[i])
        # 轮廓外接矩形面积
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        # 几何矩
        mm = cv.moments(contour)
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']
        cv.circle(img, (np.int(cx), np.int(cy)), 3, (0, 255, 0), -1)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow("mo", img)


src = cv.imread('../captcha/tupian/example.jpg')
cv.imshow('def', src)
measure_object(src)
cv.waitKey(0)
cv.destroyAllWindows()
