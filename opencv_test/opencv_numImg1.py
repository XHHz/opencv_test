# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/10 10:50
# @Author  : xhh
# @Desc    : 使用opencv自带的函数，进行处理
# @File    : opencv_numImg1.py
# @Software: PyCharm
import cv2


def inverse(img):
    img = cv2.bitwise_not(img)  # 函数实现像素点个通道值取反
    cv2.imshow('../captcha/images2', img)

src = cv2.imread('../captcha/images1/9BO0.jpg')
cv2.namedWindow('../captcha/images1/', cv2.WINDOW_AUTOSIZE)
cv2.imshow('../captcha/images1/', src)

t1 = cv2.getTickCount()  # getTickCount函数返回从操作系统启动到当前所经过的毫秒数
inverse(src)
t2 = cv2.getTickCount()  # getTickFrequency函数返回CPU的频率,就是每秒的计时周期数
time = (t2 - t1)/cv2.getTickFrequency()

print('time:%s ms' % (time*1000)) # 计算所用的时间
cv2.waitKey(0)
cv2.destroyAllWindows()