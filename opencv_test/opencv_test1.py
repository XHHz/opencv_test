# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/13 10:59
# @Author  : xhh
# @Desc    : 图片对比（https://blog.csdn.net/wc781708249/article/details/78538236?utm_source=blogkpcl15）
# @File    : opencv_test1.py
# @Software: PyCharm
import cv2

class CompareImage(object):
    def __init__(self, image_1_path, image_2_path):
        self.minimum_commutative_image_diff = 0.25
        self.image_1_path = image_1_path
        self.image_2_path = image_2_path

    def compare_image(self):
        image_1 = cv2.imread(self.image_1_path, 0)
        image_2 = cv2.imread(self.image_2_path, 0)
        img_hist_diff, img_template_diff, commutative_image_diff = self.get_image_difference(image_1, image_2)

        if img_hist_diff<0.3 and img_template_diff<0.3:
            if commutative_image_diff < self.minimum_commutative_image_diff:
                print("Matched")
                return commutative_image_diff
        return 10000 # random failure value

    @staticmethod
    def get_image_difference(image_1, image_2):
        first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
        second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

        img_hist_diff = 1-cv2.compareHist(first_image_hist, second_image_hist,0)
        img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
        img_template_diff = 1 - img_template_probability_match

        # taking only 10% of histogram diff, since it's less accurate than template method
        commutative_image_diff = (img_hist_diff / 10) + img_template_diff
        return [img_hist_diff,img_template_diff,commutative_image_diff]


if __name__ == '__main__':
    compare_image = CompareImage('../doraemon/image-003.png', '../doraemon/image-004.png')
    image_difference = compare_image.compare_image()
    print(image_difference)