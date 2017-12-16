from PIL import Image
import numpy as np
import os, cv2

_path = r'D:\Python\PycharmProjects\Michael05'

Xiaoqiao = Image.open(os.path.join(_path,'Xiaoqiao.jpg'))
pix = Xiaoqiao.load()
width = Xiaoqiao.size[0]
height = Xiaoqiao.size[1]
for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y]
        print(r,g,b)


# r,g,b = Xiaoqiao.getpixel((100,50))
# print(r,g,b)
img=cv2.imread(os.path.join(_path,'Xiaoqiao.jpg'))
img_back=cv2.imread(os.path.join(_path,'WhiteBackgroud.jpg'))
#日常缩放
rows,cols,channels = img_back.shape
img_back=cv2.resize(img_back,None,fx=0.9,fy=0.9)
cv2.imshow('img_back',img_back)


rows,cols,channels = img.shape
img=cv2.resize(img,None,fx=0.5,fy=0.5)
cv2.imshow('img',img)
# cv2.waitKey(0)
rows,cols,channels = img.shape #rows，cols最后一定要是前景图片的，后面遍历图片需要用到


hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#获取mask
lower_blue=np.array([0, 0, 0])
upper_blue=np.array([191, 189, 192])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow('Mask', mask)

#腐蚀膨胀
erode=cv2.erode(mask,None,iterations=1)
cv2.imshow('erode',erode)
dilate=cv2.dilate(erode,None,iterations=1)
cv2.imshow('dilate',dilate)


#遍历替换
center=[50,50]#在新背景图片中的位置
for i in range(rows):
    for j in range(cols):
        if dilate[i,j]==0:#0代表黑色的点
            img_back[center[0]+i,center[1]+j]=img[i,j]#此处替换颜色，为BGR通道
cv2.imshow('res',img_back)
cv2.imwrite(os.path.join(_path,'Final.jpg'), img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()