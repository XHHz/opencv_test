# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/10 10:57
# @Author  : xhh
# @Desc    : 自定义三通道，单通道图片
# @File    : opencv_numImg2.py
# @Software: PyCharm
import cv2
import numpy as np


def creat_image():
    # img = np.zeros([100, 60, 3])  # 将所有的像素点的个通道数赋值0
    # img[ :, :, 0] = np.ones([100, 60])*5
    # cv2.imshow('new_image', img)

    img = np.zeros([80, 26, 1])
    img = img*255
    cv2.imshow('new_image', img)

creat_image()
cv2.waitKey(0)
cv2.destroyAllWindows()