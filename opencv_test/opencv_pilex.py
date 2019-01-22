# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/10 14:21
# @Author  : xhh
# @Desc    : 像素的算术运算
# @File    : opencv_pilex.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt

def add_demo(img1, img2):    # 像素的加法
    dst = cv2.add(img1, img2)
    cv2.imshow("add_demo", dst)


def subtract_demo(img1, img2):  # 像素的减法
    dst = cv2.subtract(img1, img2)
    cv2.imshow("subtract_demo", dst)


def divide_demo(img1, img2):  # 像素的除法
    dst = cv2.divide(img1, img2)
    cv2.imshow("divide_demo", dst)


def multiply_demo(img1, img2):  # 像素的乘法
    dst = cv2.multiply(img1, img2)
    cv2.imshow("multiply_demo", dst)


# cv2 读取图片
src1 = cv2.imread("../captcha/tupian/kitten.jpg")
src2 = cv2.imread("../captcha/tupian/2dq7.jpg")

cv2.imshow("kitten.jpg", src1)
cv2.imshow("2dq7.jpg", src2)

add_demo(src1, src2)
subtract_demo(src1, src2)
divide_demo(src1, src1)
multiply_demo(src1, src2)

cv2.waitKey(0)
cv2.destroyAllWindows()

