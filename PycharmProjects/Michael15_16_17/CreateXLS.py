import os, json, shutil, re
from collections import OrderedDict

import xlwt

localfolder = os.path.dirname(__file__)
fileloc = os.path.join(localfolder, 'fileloc')
XLS = os.path.join(fileloc, 'XLS')
pattern = re.compile('txt')

def walk_all_txt():
    list = []
    for root, dirs, files in os.walk(fileloc):
        for child in files:
            name,type = child.split('.')
            if pattern.match(type):
                list.append(name)
    return list

def read_txt(txtfile):
    with open(txtfile,encoding='utf-8-sig') as f:
        content=f.read()
    return content

def numbers_xls(txtfile, name):
    content = read_txt(txtfile)
    jsontxt = json.loads(content,object_pairs_hook=OrderedDict)

    xls_book = xlwt.Workbook()
    xls_sheet = xls_book.add_sheet(name)

    for row, j in enumerate(jsontxt): # enumerate 对于list 特别好用
        for column, i in enumerate(j):
            xls_sheet.write(row,column,i)

    xls_book.save(os.path.join(XLS, name+'.xls'))


def city_xls(txtfile, name):
    content = read_txt(txtfile)
    jsontxt = json.loads(content, object_pairs_hook=OrderedDict)
    xls_book = xlwt.Workbook()
    xls_sheet = xls_book.add_sheet(name)

    for row, city in enumerate(jsontxt.items()):  # enumerate 对于dict
        for column, item in enumerate(city):
            xls_sheet.write(row, column, item)


    xls_book.save(os.path.join(XLS, name + '.xls'))


def student_xls(txtfile, name):
    content = read_txt(txtfile)
    jsontxt = json.loads(content, object_pairs_hook=OrderedDict)

    xls_book = xlwt.Workbook()
    xls_sheet = xls_book.add_sheet(name)

    for row, student in enumerate(jsontxt.items()):  # enumerate 对于
        for index, i in enumerate(list(student)):
            if type(i) == list:
                for column, j in enumerate(i):
                    xls_sheet.write(row, column+1, j)
            else:
                xls_sheet.write(row, 0, i)

    xls_book.save(os.path.join(XLS, name + '.xls'))

if __name__=='__main__':
    name = walk_all_txt()
    if os.path.exists(XLS):
        shutil.rmtree(XLS)
    os.mkdir(XLS)

    for i in name:
        txt_loc = os.path.join(fileloc, i + '.txt')
        if i == 'numbers':
            numbers_xls(txt_loc, i)
        if i == 'city':
            city_xls(txt_loc, i)
        if i == 'student':
            student_xls(txt_loc, i)

