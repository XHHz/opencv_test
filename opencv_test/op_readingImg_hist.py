# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/1 14:34
# @Author  : xhh
# @Desc    : 直方图均衡化, 对灰度图，彩色图都均衡化
# @File    : op_readingImg_hist.py
# @Software: PyCharm
import numpy
import cv2

image_file = '../captcha/tupian/bailing.png'
img = cv2.imread(image_file)
# 将彩色图转换为灰度图
# img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# 均衡灰度图的直方图
img_gray_histeq = cv2.equalizeHist(img_gray)


# 均衡彩色图的直方图
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# 均衡Y通道
img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
# 将其转换为BGR
img_histeq = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('img', img_gray)
cv2.imshow('img_gray_histeq', img_gray_histeq)
cv2.imshow('img_yuv', img_yuv)
cv2.imshow('img_histeq', img_histeq)
cv2.waitKey(0)