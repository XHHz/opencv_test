# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/11 9:09
# @Author  : xhh
# @Desc    : 泛洪填充
# @File    : opencv_ROI.py
# @Software: PyCharm
import cv2
import numpy as np


def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)  # opencv里的mask都为uint8类型的单通道矩阵
    image[100:300, 100:300] = 255
    cv2.imshow('fill_binary', image)
    mask = np.ones([402, 402], np.uint8) # mask值需保证比原图高宽都多2
    mask[101:301, 101:301] = 0
    cv2.floodFill(image, mask, (200, 200), (255, 0, 0), cv2.FLOODFILL_MASK_ONLY)  #
    cv2.imshow("fill_binary", image)

fill_binary()
cv2.waitKey(0)
cv2.destroyAllWindows()