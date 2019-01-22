# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/31 16:04
# @Author  : xhh
# @Desc    : 读取图片,对图片进行边缘检测，索贝尔滤波器，索贝尔垂直检测器，拉普拉斯边缘检测器，Canny边检测
# @File    : op_readingImg.py
# @Software: PyCharm

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_file = '../captcha/tupian/bailing.png'
img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

# 输入图片的大小
h, w = img.shape
#print(h,w)

# 索贝尔滤波器（边缘检测器）
sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

# 运行索贝尔垂直检测器
sobel_verrical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

# 拉普拉斯边缘检测器
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Canny边检测
canny = cv2.Canny(img, 50, 240)

#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.imshow(sobel_horizontal)
#plt.xticks([]),plt.yticks([])
#plt.show()
cv2.imshow('sobel_horizontal',sobel_horizontal )
cv2.imshow('sobel_verrical',sobel_verrical )
cv2.imshow('laplacian',laplacian )
cv2.imshow('canny',canny )

cv2.waitKey(0)