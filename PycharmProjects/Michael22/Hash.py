#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : Jenny
# @Site    : 
# @File    :
# @Software: PyCharm Community Edition
# @desc:

# 三、UUID
#
# UUID是128位的全局唯一标识符，通常由32字节的字符串表示。它可以保证时间和空间的唯一性，python中称为UUID，其他语言中可能称为GUID。
# 它通过MAC地址、时间戳、命名空间、随机数、伪随机数来保证生成ID的唯一性。
# UUID主要有五个算法，也就是五种方法来实现：
# 1、uuid1()——基于时间戳。由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
# 2、uuid2()——基于分布式计算。环境DCE（Python中没有这个函数）算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。实际中很少用到该方法。
# 3、uuid3()——基于名字的MD5散列值。通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
# 4、uuid4()——基于随机数。由伪随机数得到，有一定的重复概率，该概率可以计算出来。
# 5、uuid5()——基于名字的SHA-1散列值。算法与uuid3相同，不同的是使用 SHA-1算法。
#
# python中没有实现uuid2算法。

import uuid, hashlib

def hash_password(newpwd):
    salt = uuid.uuid4().hex
    print(hashlib.sha256(salt.encode()+newpwd.encode()).hexdigest()+salt)
    return hashlib.sha256(salt.encode()+newpwd.encode()).hexdigest()+":"+salt


def check_password(newpwd,checkpwd):
    newpwd1, salt = newpwd.split(":")
    return (newpwd1==hashlib.sha256(salt.encode()+checkpwd.encode()).hexdigest())


newpwd = input("Please enter your password : ")
newpassword=hash_password(newpwd)

checkpwd = input("Please enter again your password : ")
if check_password(newpassword,checkpwd):
    print("Passowrd is correct!")
else:
    print("the Password not same!")