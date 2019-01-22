# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/11 15:04
# @Author  : xhh
# @Desc    : 图片的直方图
# @File    : opencv_plotHist.py
# @Software: PyCharm
import cv2

# 直方图的应用，直方图均衡化（即调整图像的对比度）,直方图即统计各像素点的频次
def eaualHist_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)    # opencv的直方图均衡化要基于单通道灰度图像
    cv2.namedWindow('input_image', cv2.WINDOW_NORMAL)
    cv2.imshow('input_image', gray)
    dst = cv2.equalizeHist(gray)                # 自动调整图像对比度，把图像变得更清晰
    cv2.namedWindow("eaualHist_demo", cv2.WINDOW_NORMAL)
    cv2.imshow("eaualHist_demo", dst)


# 局部直方图均衡化
def clahe_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(5, (8, 8))
    dst = clahe.apply(gray)
    cv2.namedWindow("clahe_demo", cv2.WINDOW_NORMAL)
    cv2.imshow("clahe_demo", dst)


src = cv2.imread('../captcha/tupian/bailing.png')
eaualHist_demo(src)
clahe_demo(src)

cv2.waitKey(0)
cv2.destroyAllWindows()