# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/11 10:43
# @Author  : xhh
# @Desc    :
# @File    : opencv_gussian_noise.py
# @Software: PyCharm
import cv2
import numpy as np


# 定义像素
def clamp(pv):
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv

# 加高斯噪声
def gussian_noise(image):
    h , w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            # 获取rgb通道像素值
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv2.namedWindow('noise image', cv2.WINDOW_NORMAL)
    cv2.imshow("noise image", image)
    dst = cv2.GaussianBlur(image, (15, 15), 0)  # 高斯模糊
    cv2.namedWindow('Gaussian image', cv2.WINDOW_NORMAL)
    cv2.imshow("Gaussian image", dst)


# 读取原图，并进行展示
src = cv2.imread("../captcha/tupian/ren3.jpg")
cv2.namedWindow("原图", cv2.WINDOW_NORMAL)
cv2.imshow("原图", src)

# 进行高斯模糊
gussian_noise(src)
dst = cv2.GaussianBlur(src, (15, 15), 0)
cv2.namedWindow("高斯模糊", cv2.WINDOW_NORMAL)
cv2.imshow("高斯模糊", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()