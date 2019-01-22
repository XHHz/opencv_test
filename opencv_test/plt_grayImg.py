# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/19 15:32
# @Author  : xhh
# @Desc    : 利用 matplotlib显示灰度图
# @File    : plt_grayImg.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import matplotlib.cm as cm

img = plt.imread('../tupian/green.png')
# 将图片转化为单通道
img = img[:, :, 0]

plt.subplot(121)
plt.imshow(img)

plt.subplot(122)
# plt.colorbar()
plt.imshow(img, cmap=cm.get_cmap('winter'))

plt.show()

