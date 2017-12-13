import os
import time

def visitDir(path):
    li = os.listdir(path)
    list1 = []
    dirt_keys = ['name', 'size', 'ctime']
    dirt = {}
    for p in li:
        pathname = os.path.join(path,p)
        list1.append(pathname)
        pathsize = os.stat(pathname).st_size
        list1.append(str(pathsize))
        pathctime = time.strftime("%Y-%m-%d %X", time.localtime(os.stat(pathname).st_ctime))
        list1.append(pathctime)

        if os.path.isfile(pathname):
            dirt = zip(dirt_keys, list1)
            print(list(dirt))
        else:
            visitDir(pathname)

if __name__ == '__main__':
    path = r"D:\Python\PycharmProjects"
    visitDir(path)


