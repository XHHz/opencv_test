# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/19 15:56
# @Author  : xhh
# @Desc    : 得到灰度图以及直方图
# @File    : opencv_grayimg_hist.py
# @Software: PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../tupian/green.png')
# img = cv2.imread('../dataset/100201.png')
# cv2.imshow('img', img)

# 2*g-r-b分离土壤与绿色植物
# 转化为浮点数进行计算
fimg = np.array(img, dtype=np.float32)/255
(b, g, r) = cv2.split(fimg)
gray_img = 2*g - r -b

# 求取最大值和最小值
(minVal, maxVal, minLoc, macLoc) = cv2.minMaxLoc(gray_img)

# 计算直方图
hist = cv2.calcHist([gray_img],[0],None,[255],[minVal, maxVal])
# 展示直方图
# plt.plot(hist)
# plt.show()

# 转换为u8类型，进行otsu二值化
gray_u8 = np.array((gray_img - minVal) / (maxVal - minVal) * 255, dtype=np.uint8)
(thresh, bin_img) = cv2.threshold(gray_u8, -1.0, 255, cv2.THRESH_OTSU)
# cv2.imshow('bin_img', bin_img)

# 得到彩色的图像
(b8, g8, r8) = cv2.split(img)
color_img = cv2.merge([b8 & bin_img, g8 & bin_img, r8 & bin_img])
cv2.imshow('color_img',color_img)

cv2.waitKey(0)