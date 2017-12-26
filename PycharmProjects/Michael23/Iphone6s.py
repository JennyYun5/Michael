#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : Jenny
# @Site    : 
# @File    : 
# @Software: PyCharm Community Edition
# @desc:

import os, re, shutil
from PIL import Image


# iPhone6s
iPhone_W = 1080
iPhone_H = 1920

img_path = os.path.join(os.path.dirname(__file__),'image')
img_out = os.path.join(os.path.dirname(__file__),'image_out')
pattern = re.compile(r'(.jpg)$')

def resize(img, img_out):
    imgin = Image.open(img)
    w, h = imgin.size
    if w > iPhone_W:
        w = iPhone_W
        h = iPhone_W//w*h
    if h > iPhone_H:
        h = iPhone_H
        w = iPhone_H//h*w
    img_size = imgin.resize((w, h),Image.ANTIALIAS)
    img_size.save(img_out)


def get_all_image():
    for root, dirs, files in os.walk(img_path):
        for file in files:
            name, type = os.path.splitext(file)
            if pattern.match(type):
                img = os.path.join(root, file)
                img_out1 = os.path.join(img_out,"Iphone6s_"+file)
                resize(img, img_out1)

if __name__=="__main__":
    if os.path.exists(img_out):
        shutil.rmtree(img_out)
    os.mkdir(img_out)
    get_all_image()

