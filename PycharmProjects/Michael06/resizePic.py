import os
import re

from os.path import getsize, join

from PIL import Image

iPhone_W = 640
iPhone_H = 1136
# print(os.path.dirname(__file__))  # D:/Python/PycharmProjects/Michael06
Picfloder = os.path.join(os.path.dirname(__file__), 'Pic')
PicfloderO = os.path.join(os.path.dirname(__file__), 'Pic_Out')
Picfloder1 = os.path.join(os.path.dirname(__file__), 'Pic_Out1')
pattern = re.compile(r'(.jpg|.png)$')
# for root, dirs, files in os.walk(Picfloder):
#         # print(root, "consumes", end="")
#         # print(sum([getsize(join(root, name)) for name in files]), end="")
#         # print("bytes in", len(files), "non-directory files")
#         # D: / Python / PycharmProjects / Michael06\Pic
#         # consumes1025515bytes in 3 non - directory files
#         # print(root, dirs, files)
#         # D: / Python / PycharmProjects / Michael06\Pic['Peng']['Wangzhe.jpg', 'Wangzhe02.jpg', 'Wangzhe03.jpg']
#         # D: / Python / PycharmProjects / Michael06\Pic\Peng['Yue']['Peng01.jpg', 'Peng02.jpg', 'Peng03.jpg', 'Thumbs.db']
#         # D: / Python / PycharmProjects / Michael06\Pic\Peng\Yue[]['Thumbs.db', 'Yue01.jpg', 'Yue02.jpg', 'Yue03.jpg']
#         for file in files:
#                 # print(os.path.splitext(file))
#                 # ('Wangzhe', '.jpg')
#                 # ('Wangzhe02', '.jpg')
#                 # ('Wangzhe03', '.jpg')
#                 name, type = os.path.splitext(file)
#                 if pattern.match(type):
#                         inImage = os.path.join(root, file)
#                         outImage = os.path.join(PicfloderO, 'Iphone_'+file)
#                         inPic = Image.open(inImage)
#                         w, h = inPic.size
#                         if w > iPhone_W:
#                                 w = iPhone_W
#                                 h = iPhone_W//w*h
#                         if h > iPhone_H:
#                                 h = iPhone_H
#                                 w = iPhone_H//h*w
#
#                         OutPic = inPic.resize((w, h), Image.ANTIALIAS)
#                         OutPic.save(outImage)
#                         # Image.ANTIALIAS 抗锯齿过滤属性， 保存图片质量， 避免因为改动而失真


def Resize(Picfloder):
        file2 = os.listdir(Picfloder) # 注意这个的放置位置
        for f in file2:
                f1 = os.path.join(Picfloder, f)
                print(f)
                if os.path.isdir(f1):
                        Resize(f1)
                else:
                        name, type = os.path.splitext(f1)
                        if pattern.match(type):
                                sourceout = os.path.join(Picfloder1, 'V2_'+f)
                                fin = Image.open(f1)
                                w, h = fin.size
                                if w > iPhone_W:
                                        w = iPhone_W
                                        h = iPhone_W//w*h
                                if w > iPhone_H:
                                        h = iPhone_H
                                        w = iPhone_H//h*w
                                fout = fin.resize((w,h), Image.ANTIALIAS)
                                fout.save(sourceout)


if __name__=='__main__':
        Resize(Picfloder)

