# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/11 15:33
# @Author  : xhh
# @Desc    : 图片二值化处理, 将图片像素进行0或255处理
# @File    : opencv_threshold.py
# @Software: PyCharm
import cv2
import numpy as np


# 全局阈值
def threshold_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # 将图像进行灰度处理
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    print("全局阈值%s" % ret)
    cv2.namedWindow('binary0', cv2.WINDOW_NORMAL)
    cv2.imshow('binary0', binary)


# 局部阈值
def local_threshold_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
    cv2.namedWindow('binary1', cv2.WINDOW_NORMAL)
    cv2.imshow('binary1', binary)


# 用户自己计算阈值
def custom_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])
    mean = m.sum()/(w*h)
    print('mean:', mean)
    ret, binary = cv2.threshold(gray, mean, 255, cv2.THRESH_BINARY)
    cv2.namedWindow('bianry2', cv2.WINDOW_NORMAL)
    cv2.imshow('bianry2',binary)


src = cv2.imread("../captcha/tupian/example.jpg")
cv2.namedWindow('bianry2', cv2.WINDOW_NORMAL)
cv2.imshow('bianry2', src)

threshold_demo(src)
local_threshold_demo(src)
custom_demo(src)

cv2.waitKey(0)
cv2.destroyAllWindows()
