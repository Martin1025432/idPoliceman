# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:38:33 2017

@author: Administrator
"""

#coding:utf-8
#===============================================
#文件说明:
#       第三节:图像处理---之---在python下,怎样使用OpenCv设置ROI区域
#开发环境：
#       Ubuntu14.04+Python2.7+IDLE+IPL
#时间地点:
#       陕西师范大学　2016.11.19
#作　　者:
#       九月
#===============================================

#1--Python中ROI区域的设置也是使用Numpy中的索引来实现的
import cv2
import numpy as np
import matplotlib.pyplot as plt 
 
srcImg = cv2.imread("test.bmp")
#plt.imshow(srcImg, cmap="gray")

#cv2.imshow 必须跟随 cv2.waitKey(0)
#cv2.imshow("[srcImg]",srcImg)                  #[1]显示原始图片
roiImag=srcImg[300:500,250:550] 
srcImg[0:180,0:300]=roiImag
plt.imshow(srcImg, cmap="gray")
#cv2.waitKey(0)