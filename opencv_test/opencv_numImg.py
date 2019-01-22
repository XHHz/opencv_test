# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/10 10:19
# @Author  : xhh
# @Desc    : 遍历访问图片的每个像素点，应修改RGB, 使用数组进行操作
# @File    : opencv_numImg.py
# @Software: PyCharm
import cv2

# 遍历访问图片的每个像素点，应修改RGB
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print('高度%s,宽度%s,通道%s' % (height, width, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]  # 获取像素点的每个通道的数值
                image[row, col, c] = 255 - pv  # 灰度值是0-255，修改每个通道像素的灰度
    cv2.imshow('../captcha/images2', image)
    cv2.imwrite('../captcha/images2/0JEb.jpg', image)


src = cv2.imread('../captcha/images1/0JEb.jpg')  # RGB三通道
cv2.namedWindow('../captcha/images1/', cv2.WINDOW_AUTOSIZE)
cv2.imshow('../captcha/images1/', src)

t1 = cv2.getTickCount()  # getTickCount函数返回从操作系统启动到当前所经过的毫秒数
access_pixels(src)
t2 = cv2.getTickCount()  # getTickFrequency函数返回CPU的频率,就是每秒的计时周期数
time = (t2 - t1)/cv2.getTickFrequency()

print('time:%s ms' % (time*1000))  # 计算所用的时间
cv2.waitKey(0)
cv2.destroyAllWindows()


