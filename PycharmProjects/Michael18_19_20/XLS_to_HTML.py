#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : Jenny
# @Site    : 
# @File    : 
# @Software: PyCharm Community Edition
# @desc:
import os, re, xlwt
from xml.dom.minidom import Document
import xlrd

xls_folder = 'D:\Python\PycharmProjects\Michael18_19_20\XLS'
xml_folder = 'D:\Python\PycharmProjects\Michael18_19_20\XLS\XML'
xls_pattern = re.compile('xls')


def read_xls_content(xls_name):
    xls_open = xlrd.open_workbook(os.path.join(xls_folder, xls_name+'.xls'))
    xls_sheet = xls_open.sheet_by_name(xls_name)
    list = []
    for i in range(xls_sheet.nrows):
        xls_data = xls_sheet.row_values(i)
        list.append(xls_data)

    return list


def student_to_html(list, xls_name):
    doc = Document() # 空文档
    root = doc.createElement('root') # 根节点
    child = doc.createElement('values')  # 创建节点
    root.appendChild(child)
    doc.appendChild(root)
    comment_node = doc.createComment('comment is here!') # 如果不加这一行， 那个value 的那个在同一行
    child.appendChild(comment_node)
    nodetxt = doc.createTextNode(str(list))
    child.appendChild(nodetxt)
    print(doc.toprettyxml(indent='\t',encoding='utf-8'))

    with open(os.path.join(xml_folder, xls_name+'.xml'), 'w') as f:
        doc.writexml(f,indent='\t', addindent='\t', newl='\n', encoding="utf-8")

def city_to_html(list, xls_name):
    pass


def numbers_to_html(list, xls_name):
    pass

if __name__=='__main__':
    for root, dir, files in os.walk(xls_folder):
        for f1 in files:
            xls_name, type = f1.split('.')
            if type == 'xls':
                if xls_name == 'student':
                    list = read_xls_content(xls_name)
                    print(list)
                    student_to_html(list, xls_name)
                if xls_name == 'city':
                    list = read_xls_content(xls_name)
                    print(list)
                    student_to_html(list, xls_name)
                    # city_to_html(list, xls_name)
                if xls_name == 'numbers':
                    list = read_xls_content(xls_name)
                    print(list)
                    student_to_html(list, xls_name)
                    # numbers_to_html(list, xls_name)



