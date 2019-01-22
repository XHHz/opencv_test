# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/1 15:01
# @Author  : xhh
# @Desc    : 检测棱角
# @File    : op_reading_harris.py
# @Software: PyCharm
import numpy as np
import cv2

image_file = '../captcha/tupian/dongman.png'
img = cv2.imread(image_file)

# 将彩色图转换为灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# 将图像转化为灰度图，并将其强制转化为浮点值
img_gray = np.float32(img_gray)

# 哈里斯角检验器
img_harris = cv2.cornerHarris(img_gray, 7, 5, 0.04)
# 放大图片标记棱角
img_harris = cv2.dilate(img_harris, None)
# 用阈值显示棱角
img[img_harris > 0.01 * img_harris.max()] = [0, 0 , 0]

# cv2.imshow('img_gray', img_gray)
cv2.imshow('img', img)
cv2.waitKey(0)