# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/11 14:30
# @Author  : xhh
# @Desc    : 图像的直方图
# @File    : opencv_plot.py
# @Software: PyCharm
import cv2
from matplotlib import pyplot as plt


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])  # ravel函数将多维数组降为一维数组
    plt.show()


def image_hist(image):
    color = ('b', 'g', 'r')
    for i, color in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])  # 计算直方图
        plt.plot(hist, color)
        plt.xlim([0, 256])
    plt.show()


src = cv2.imread("../captcha/tupian/example.jpg")
cv2.namedWindow('src', cv2.WINDOW_NORMAL)
cv2.imshow('src', src)

plot_demo(src)
image_hist(src)

cv2.waitKey(0)
cv2.destroyAllWindows()
