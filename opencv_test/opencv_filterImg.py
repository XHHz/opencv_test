# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/19 15:42
# @Author  : xhh
# @Desc    : 图片滤波器
# @File    : opencv_filterImg.py
# @Software: PyCharm
import cv2
import numpy as np

# filter2D
img = cv2.imread('../tupian/green.png')
cv2.imshow('src', img)

 # 直接给出图片的滤波矩阵
kernel = np.array([ [-1, -1, -1],
                    [-1,  8, -1],
                    [-1, -1, -1] ])

filter_dst = cv2.filter2D(img, -1, kernel)

cv2.imshow('dst', filter_dst)
cv2.waitKey(0)
