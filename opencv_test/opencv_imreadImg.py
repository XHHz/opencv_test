# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/19 14:59
# @Author  : xhh
# @Desc    : 读取图片,并利用matplotlib
# @File    : opencv_imreadImg.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../tupian/green.png")
# 修改图片通道
(r, g, b) = cv2.split(img)
img = cv2.merge([b, g, r])

#plt.imshow(img)
#plt.show()

img1 = cv2.imread('../tupian/green.png')
img2 = plt.imread('../tupian/green.png')

plt.subplot(121)
plt.imshow(img1)

plt.subplot(122)
plt.imshow(img2)

plt.show()


