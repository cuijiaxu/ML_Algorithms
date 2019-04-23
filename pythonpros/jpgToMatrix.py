import os
import numpy as np
from PIL import Image
from pylab import *

#此函数读取特定文件夹下的jpg格式图像地址信息，存储在列表中
def get_imglist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

# r""是防止字符串转译
# c=['zheng_chang\\1.jpg', 'zheng_chang\\2.jpg', 'zheng_chang\\3.jpg']  以list形式输出jpg格式的所有图像（带路径）

c = get_imglist(r"testjpg")
d = len(c)
data = np.empty((1, 256*256*3))  # 建立d*（1,256*256*3）的随机矩阵

#遍历图片
for i in range(d):
    img = Image.open(c[i])
    img_ndarray = np.asarray(img)
    print(img_ndarray.shape)
    #img_ndarray = np.asarray(img,dtype='float64')/256 #图像转化为数组，并将像素转化到0-1之间
    #data = np.ndarray.flatten(img_ndarray) #将图像的矩阵形式转化为一维数组保存到data
    #A= np.array(data).reshape(256,256*3) #数组转矩阵
    #savetxt('0_%d.txt'%i,A,fmt="%.2f",delimiter=',') #进行存储保存为两位小数，数据“，“分隔

