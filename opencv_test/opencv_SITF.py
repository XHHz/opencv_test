# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/31 16:26
# @Author  : xhh
# @Desc    : SITF检测特征点
# @File    : opencv_SITF.py
# @Software: PyCharm
import numpy as np
import cv2

# 读取图片
input_file = '../doraemon/image-030.png'
img = cv2.imread(input_file)
img_gray = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
# 提取特征点
sift = cv2.xfeatures2d.SURF_create()
keypoints = sift.detect(img_gray, None)
img_sift = np.copy(img_gray)

cv2.drawKeypoints(img, keypoints, img_sift, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('input_image',img_gray)
cv2.imshow('img_sift', img_sift)
cv2.waitKey(0)

