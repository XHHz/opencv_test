# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/11 11:17
# @Author  : xhh
# @Desc    : 边缘保留滤波
# @File    : opencv_EPF.py
# @Software: PyCharm
import cv2
import numpy as np


# 双边滤波
def bi_demo(image):
    """
        双边滤波函数原型：bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) -> dst
        src: 表示待处理的输入图像
        d : 参数表示在过滤期间使用的每个像素邻域的直径。如果输入d非0，则sigmaSpace由d计算得出，
            如果sigmaColor没输入，则sigmaColor由sigmaSpace计算得出。
        sigmaColor : 表示色彩空间的标准方差，一般尽可能大。较大的参数值意味着像素邻域内较远的颜色会混合在一起，从而产生更大面积的半相等颜色。
        sigmaSpace : 表示坐标空间的标准方差(像素单位)，一般尽可能小。参数值越大意味着只要它们的颜色足够接近，
        越远的像素都会相互影响。当d > 0时，它指定邻域大小而不考虑sigmaSpace。 否则，d与sigmaSpace成正比。
    """
    dst = cv2.bilateralFilter(image, 0, 100, 15)
    cv2.namedWindow('bi_demo', cv2.WINDOW_NORMAL)
    cv2.imshow('bi_demo', dst)


# 均值迁移
def shift_demo(image):
    """
        均值漂移pyrMeanShiftFiltering函数原型：pyrMeanShiftFiltering(src, sp, sr[, dst[, maxLevel[, termcrit]]]) -> dst
        src : 表示输入图像，8位，三通道图像。
        sp : 表示漂移物理空间半径大小。
        sr : 表示漂移色彩空间半径大小。
        dst : 表示和源图象相同大小、相同格式的输出图象。
        maxLevel : 表示金字塔的最大层数。
        termcrit : 表示漂移迭代终止条件。
    """
    dst = cv2.pyrMeanShiftFiltering(image, 10, 50)
    cv2.namedWindow('shift_demo', cv2.WINDOW_NORMAL)
    cv2.imshow('shift_demo', dst)


src = cv2.imread("../captcha/tupian/lean.jpg")
cv2.namedWindow('input_image', cv2.WINDOW_NORMAL)
cv2.imshow('input_image', src)

bi_demo(src)
shift_demo(src)

cv2.waitKey(0)
cv2.destroyAllWindows()
