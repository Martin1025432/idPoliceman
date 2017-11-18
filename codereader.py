# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:48:40 2017

@author: Administrator
"""

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
#import cv2
#import numpy as np
#import matplotlib.pyplot as plt 
##以灰度读取图片
##srcImg = cv2.imread("CZ180.jpg",0)
#srcImg = cv2.imread("CZ180.jpg")
#
#
##roiImag=srcImg[800:1200,0:800] 
#imgray = cv2.cvtColor(srcImg,cv2.COLOR_BGR2GRAY)#转成灰色图
#plt.imshow(imgray, cmap="gray")
#
##二值化 ,找轮廓前必须先把图像二值化    
#ret, gray = cv2.threshold(imgray, 150, 250, cv2.THRESH_BINARY)
#plt.imshow(gray)

#coding=utf-8  
import cv2  
import numpy as np    
  
img = cv2.imread("CZ180.jpg", 0)  
cv2.imshow("aDDbsX", img)    
x = cv2.Sobel(img,cv2.CV_16S,1,0)  
y = cv2.Sobel(img,cv2.CV_16S,0,1)  
  
absX = cv2.convertScaleAbs(x)   # 转回uint8  
absY = cv2.convertScaleAbs(y)  
  
dst = cv2.addWeighted(absX,0.5,absY,0.5,0)  
  
cv2.imshow("absX", absX)  
cv2.imshow("absY", absY)  
  
cv2.imshow("Result", dst)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()   




#gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
#gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)
#plt.imshow(gray)
##cv2.imshow("[sImg]",thresh)   
#找轮廓必须有三个返回值，网上教程大部份出错
#thresh,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
