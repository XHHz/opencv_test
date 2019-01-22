# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/11 10:23
# @Author  : xhh
# @Desc    : 均值模糊、中值模糊、自定义模糊   模糊是卷积的一种表象
# @File    : opencv_noise.py
# @Software: PyCharm
import cv2
import numpy as np


def blur_demo(image):      # 均值模糊  去随机噪声有很好的去燥效果
    dst = cv2.blur(image, (1, 15))    #（1, 15）是垂直方向模糊，（15， 1）还水平方向模糊
    cv2.namedWindow('blur_demo', cv2.WINDOW_NORMAL)
   #  cv2.imwrite("../captcha/tupian/", image)
    cv2.imshow("blur_demo", dst)


def median_blur_demo(image):    # 中值模糊  对椒盐噪声有很好的去燥效果
    dst = cv2.medianBlur(image, 5)
    cv2.namedWindow('median_blur_demo', cv2.WINDOW_NORMAL)
    cv2.imshow("median_blur_demo", dst)


def custom_blur_demo(image):    # 用户自定义模糊
    kernel = np.ones([5, 5], np.float32)/25   #除以25是防止数值溢出
    dst = cv2.filter2D(image, -1, kernel)
    cv2.namedWindow('custom_blur_demo', cv2.WINDOW_NORMAL)
    cv2.imshow("custom_blur_demo", dst)


src = cv2.imread('../captcha/tupian/ren3.jpg')
cv2.namedWindow('input_image', cv2.WINDOW_NORMAL)
cv2.imshow('input_image', src)

blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)

cv2.waitKey(0)
cv2.destroyAllWindows()