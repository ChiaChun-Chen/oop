# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# coding=gbk
from PIL import Image
import numpy as np
# import scipy
import matplotlib.pyplot as plt

def ImageToMatrix(filename):
    # 读取图片
    im = Image.open(filename)
    # 显示图片
#     im.show()  
    width,height = im.size
    im = im.convert("L") 
    data = im.getdata()
    data = np.matrix(data,dtype='int')/255
    #new_data = np.reshape(data,(width,height))
    new_data = np.reshape(data,(height,width))
    return new_data
#     new_im = Image.fromarray(new_data)
#     # 显示图片
#     new_im.show()
def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im



filename = "level1.bmp"
data = ImageToMatrix(filename)
print(data)
print(type(data))
np.savetxt("level1.txt", data)
np.savetxt("level1.csv", data, delimiter=",")
'''
data_string=','.join(data)
matrix = open("123.txt","w")
matrix.write(data_string)
matrix.close()
'''
new_im = MatrixToImage(data)
plt.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
new_im.show()
new_im.save("level1.bmp")
