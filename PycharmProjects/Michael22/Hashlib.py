#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : Jenny
# @Site    : 
# @File    : 
# @Software: PyCharm Community Edition
# @desc:

import hashlib
print("algorithms_available方法列出了系统中可用的所有算法")
print(hashlib.algorithms_available)
print("algorithms_guaranteed只列出模块中存在的算法")
print(hashlib.algorithms_guaranteed)

# MD5
print(hashlib.md5(b'Hello world!').hexdigest())
# 86fb269d190d2c85f6e0468ceca42a20

myhash = input("Please enter your string :") # 123
print(hashlib.md5(myhash.encode()))
# <md5 HASH object @ 0x010D66C8>


# SHA1
print(hashlib.sha1(b'Hello world!').hexdigest())
# d3486ae9136e7856bc42212385ea797094475802

# SHA224
print(hashlib.sha224(b'Hello world!').hexdigest())
# 7e81ebe9e604a0c97fef0e4cfe71f9ba0ecba13332bde953ad1c66e4

# SHA256
print(hashlib.sha256(b'Hello world!').hexdigest())
# c0535e4be2b79ffd93291305436bf889314e4a3faec05ecffcbb7df31ad9e51a

# SHA384
print(hashlib.sha384(b'Hello world!').hexdigest())
# 86255fa2c36e4b30969eae17dc34c772cbebdfc58b58403900be87614eb1a34b8780263f255eb5e65ca9bbb8641cccfe

# SHA512
print(hashlib.sha512(b'Hello world!').hexdigest())
# f6cde2a0f819314cdde55fc227d8d7dae3d28cc556222a0a8ad66d91ccad4aad6094f517a2182360c9aacf6a3dc323162cb6fd8cdffedb0fe038f55e85ffb5b6

# 更多关于安全密码的信息
# 下面的 python 程序演示了如何使用 salt 加 hash 来单向转换密码明文


