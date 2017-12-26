#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : Jenny
# @Site    : 
# @File    : # @Software: PyCharm Community Edition
# @desc:
import pandas as pd
import matplotlib.pyplot as plt

filepath = 'D:\Python\PycharmProjects\Michael21\DataAnalyst.csv'
df = pd.read_csv(filepath,encoding='gb2312')
# print(df.info())  # 可以显示csv中有那些列， 及属性， 一些必要信息
print('-'*40)
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 6876 entries, 0 to 6875
    # Data columns (total 17 columns):
    # city                 6876 non-null object
    # companyFullName      6876 non-null object
    # companyId            6876 non-null int64
    # companyLabelList     6170 non-null object
    # companyShortName     6876 non-null object
    # companySize          6876 non-null object
    # businessZones        4873 non-null object
    # firstType            6869 non-null object
    # secondType           6870 non-null object
    # education            6876 non-null object
    # industryField        6876 non-null object
    # positionId           6876 non-null int64
    # positionAdvantage    6876 non-null object
    # positionName         6876 non-null object
    # positionLables       6844 non-null object
    # salary               6876 non-null object
    # workYear             6876 non-null object
    # dtypes: int64(2), object(15)
    # memory usage: 510.4+ KB
    # None

# print(df.positionId.unique())  # 原来显示 # positionId           6876 non-null int64
# print(len(df.positionId.unique())) # 唯一的话， 只有5031 条，说明有重复的

df_duplicates = df.drop_duplicates(subset='positionId',keep='first').head() # 数据去重
# print(len(df_duplicates)) # 只有5031 条 , 而且df_duplicates 打印的时候跟原表样子一样， 格式不好看
# print(df_duplicates.head(10)) # 显示前 10 条数据
# print(df_duplicates.tail(5))  # 显示后 5 条数据

def cut_word(word, method):
    pos = word.find('-')
    length = len(word)
    if pos == -1:
        word1 = word.split('以')
        bottom_salary = word[:word1[0].upper().find('K') - 1]
        top_salary = bottom_salary
    else:
        bottom_salary = word[:pos - 1]
        top_salary = word[pos + 1:length - 1]
    if method == 'top':
        return str(top_salary)
    else:
        return str(bottom_salary)


df_duplicates['topSalary'] = df_duplicates.salary.apply(cut_word,method='top')
df_duplicates['bottomSalary'] = df_duplicates.salary.apply(cut_word,method='bottom')
# print(df_duplicates['topSalary'].head()) # 显示Salary 的最大， 最小范围

df_duplicates.topSalary = df_duplicates.topSalary.astype('int') # 数据类型转换为数字
df_duplicates.bottomSalary = df_duplicates.bottomSalary.astype('int') # 数据类型转换为数字
# axis=1表示将函数用在行，axis=0则是列
df_duplicates['aveSalary'] = df_duplicates.apply(lambda x:(x.topSalary+x.bottomSalary)/2,axis = 1)

# 切选出我们想要的内容进行后续分析
df_clean = df_duplicates[['city','companyShortName','companySize',
                          'education','positionName','positionLables',
                          'workYear','aveSalary']]
# print(df_clean.head())
# 对city 非零的值进行计数
# print(df_clean.city.value_counts())
# 它能快速生成各类统计指标。
# 数据分析师的薪资的平均数是7k，中位数是7k，两者相差不大，最大薪资在12.5k
# print(df_clean.describe())

# 使用R语言中的ggplot2配色作为绘图风格
plt.style.use('ggplot')
df_clean.aveSalary.hist() # 绘制直方图  df_clean.avgSalary.hist(bins=15) 宽距缩小
# 观察不同城市、不同学历对薪资的影响。箱线图是最佳的观测方式





