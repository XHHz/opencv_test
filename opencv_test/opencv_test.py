# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/12 15:26
# @Author  : xhh
# @Desc    :
# @File    : opencv_test.py
# @Software: PyCharm
import datetime
import heapq

import os

import cv2
import nanopq
import numpy as np
import shutil


def dHash(gray, height):
    #缩放8*8
    # gray=cv2.resize(img,(64,63),interpolation=cv2.INTER_CUBIC)
    #转换灰度图
    # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash_str=''
    #每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(height):
        for j in range(height):
            if gray[i,j]>gray[i,j+1]:
                hash_str=hash_str+'1'
            else:
                hash_str=hash_str+'0'
    return hash_str

def pq_dis():
    N, D = 10000, 128
    X = np.random.random((N, D)).astype(np.float32)  # 10,000 128-dim vectors
    query = np.random.random((D,)).astype(np.float32)  # a 128-dim vector

    # Instantiate with M=8 sub-spaces
    #pq = nanopq.PQ(M=8,Ks=256)
    pq = nanopq.PQ(M=8,Ks=256)

    # Train with the top 1000 vectors
    pq.fit(X[:1000])

    # Encode to PQ-codes
    X_code = pq.encode(X)  # (10000, 8) with dtype=np.uint8
    time1=datetime.datetime.now()
    # Results: create a distance table online, and compute Asymmetric Distance to each PQ-code
    dists = pq.dtable(query).adist(X_code)

    nsmallestList = heapq.nsmallest(5, dists)
    print(nsmallestList)
    indexs=[dists.tolist().index(i) for i in nsmallestList]
    print(indexs)
    print(dists[indexs])
    print("time",(datetime.datetime.now()-time1).microseconds)

if __name__ == '__main__':
    path=r"../cat1"
    files=os.listdir(path)

    datas=[]
    for file in files:
        img_1=cv2.imread(path+"/"+file,0)
        img1 = cv2.resize(img_1, (65, 64), interpolation=cv2.INTER_LINEAR)
        dhash=dHash(img1,64)
        data= list(map(int,dhash))
        datas.append(data)
    datas=np.asarray(datas,dtype=np.float32)
    N=len(datas)
    D=64*64

    query =datas[0]
    # np.random.random((D,)).astype(np.float32)  # a 128-dim vector

    # Instantiate with M=8 sub-spaces
    pq = nanopq.PQ(M=8,Ks=48)

    # Train with the top 1000 vectors
    pq.fit(datas)

    # Encode to PQ-codes
    X_code = pq.encode(datas)  # (10000, 8) with dtype=np.uint8

    time1=datetime.datetime.now()
    # Results: create a distance table online, and compute Asymmetric Distance to each PQ-code
    dists = pq.dtable(query).adist(X_code)

    nsmallestList = heapq.nsmallest(54, dists)
    print(nsmallestList)
    indexs=[dists.tolist().index(i) for i in nsmallestList]
    print(indexs)
    for i in indexs:
        print(files[i])
        shutil.copy(path+"/"+files[i], "out/"+str(dists[i])+"_"+files[i])
    print("time",(datetime.datetime.now()-time1).microseconds)
