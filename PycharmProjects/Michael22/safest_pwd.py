#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : Jenny
# @Site    : 
# @File    : 
# @Software: PyCharm Community Edition
# @desc:
import os
from hashlib import sha256
from hmac import HMAC

def encrypt_pwd(pwd, salt=None):
    if salt==None:
        salt = os.urandom(8) # 生成一个八个byte的随机串作为salt
    assert len(salt)==8
    assert isinstance(salt, bytes)
    assert isinstance(pwd, str)

    if isinstance(pwd, str):
        pwd = pwd.encode("utf-8")
    assert isinstance(pwd, bytes)

    print(pwd)
    for i in range(10):
        result = HMAC(pwd, salt, sha256).digest()
    return salt+result


def check_pwd(pwd, oldpwd):
    return pwd == encrypt_pwd(oldpwd, salt=pwd[:8]) # 切片


if __name__=='__main__':
    pwd = encrypt_pwd("Michael")
    assert check_pwd(pwd, "Michael")

