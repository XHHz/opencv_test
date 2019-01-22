# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/10 10:03
# @Author  : xhh
# @Desc    :
# @File    : op_readimg.py
# @Software: PyCharm
import cv2
import numpy as np

img_captcha = cv2.imread("../captcha/tupian/green.png", cv2.IMREAD_GRAYSCALE)
height = len(img_captcha)
width = len(img_captcha[0])
# 对图片进行裁剪
gray_image = img_captcha[0:60, 0:100]
# 进行存储处理后的图片
cv2.imwrite('../captcha/tupian/green.jpg',gray_image)

#  裁剪后的图片大小
height=len(gray_image)
width = len(gray_image[0])
print('图片大小%d, %d'%(width, height))
print('图片size',gray_image.size)
print('图片dtype',gray_image.dtype)
pixel_data = np.array(gray_image)
print('图片矩阵对象',pixel_data)
print('图片大小',gray_image.shape)
cv2.imshow('green.jp', gray_image)
cv2.imshow('green.png',gray_image)
# 在图片显示后是否立即停止
cv2.waitKey(0)