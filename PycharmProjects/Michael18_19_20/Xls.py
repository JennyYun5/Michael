#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : Jenny
# @Site    : 
# @File    : 
# @Software: PyCharm Community Edition
# @desc:

import xlrd

fname = "D:\Python\PycharmProjects\Michael18_19_20\XLS\city.xls"
bk = xlrd.open_workbook(fname)
print(bk) # <xlrd.book.Book object at 0x01968330>
shxrange = range(bk.nsheets)
print(shxrange) # range(0, 1)
try:
    sh = bk.sheet_by_name("city")
except:
    print("no sheet in %s named Sheet1" % fname)
nrows = sh.nrows # 获取行数
ncols = sh.ncols # 获取列数
print("nrows %d, ncols %d" % (nrows, ncols)) # nrows 3, ncols 2
# 获取第一行第一列数据
cell_value = sh.cell_value(1, 1)
print(cell_value) # 北京

row_list = []
# 获取各行数据
for i in range(1, nrows):
    row_data = sh.row_values(i)
    row_list.append(row_data)
print(row_list)  # [['4', '北京'], ['9', '成都']]
