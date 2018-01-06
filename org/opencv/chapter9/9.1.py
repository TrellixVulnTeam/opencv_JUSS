"""
9.1获取并修改像素值
"""
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\lee\\Desktop\\1.jpg")
#根据像素的行和列的坐标获取他的像素值
#1、对于BGR图像，返回其BGR值
px = img[100,100]
print(px)
#2、对于灰度图像，返回其灰度值
blue = img[100,100,0]
print(blue)

print('---------------------')
#可以用像素的行和列的坐标来修改像素值
img[100,100] = [255,255,255]
print(img[100,100])

"""
Numpy 是经过优化了的进行快速矩阵运算的软件包。所以我们不推荐
逐个获取像素值并修改，这样会很慢，能有矩阵运算就不要用循环
"""
"""
上面提到的方法被用来选取矩阵的一个区域，比如说前5 行的后3
列。对于获取每一个像素值，也许使用Numpy 的array.item() 和array.
itemset() 会更好。但是返回值是标量。如果你想获得所有B，G，R 的
值，你需要使用array.item() 分割他们。
"""
print('---------------------')
#获取像素更好的方法
print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))

"""
img[100,100,2](y轴像素点数， x轴像素点数，图像通道数)
B --- 0
G --- 1
R --- 2
图像通道，在RGB色彩模式下就是指那单独的红色、绿色、蓝色部分。
也就是说，一幅完整的图像，是由红色绿色蓝色三个通道组成的。他们共同作用产生了完整的图像。
"""