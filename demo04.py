#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 经典排序算法总结与实现 --- python


__author__ = 'Bobby'

"""
 冒泡排序 BubbleSort
 
 介绍:

冒泡排序的原理非常简单,它重复地走访过要排序的数列,一次比较两个元素,如果他们的顺序错误就把他们交换过来.

步骤:

比较相邻的元素.如果第一个比第二个大,就交换他们两个.
对第0个到第n-1个数据做同样的工作.这时，最大的数就“浮”到了数组最后的位置上。
针对所有的元素重复以上的步骤,除了最后一个。
持续每次对越来越少的元素重复上面的步骤,直到没有任何一对数字需要比较。

不过针对上述代码还有两种优化方案。

优化1:某一趟遍历如果没有数据交换,则说明已经排好序了,因此不用再进行迭代了.用一个标记记录这个状态即可.
优化2:记录某次遍历时最后发生数据交换的位置,这个位置之后的数据显然已经有序,
不用再排序了.因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了.

"""


#---------------------------------------
#   程序：冒泡排序
#   版本：0.1
#   作者：Bobby
#   日期：2017-06-03
#   语言：Python 2.7.10
#   说明：冒泡排序,从小到大排序,以及加了两种优化
#---------------------------------------

import datetime

def bubble_sort(arry):
    n=len(arry)             # 获得数组的长度
    for i in range(n-1,0,-1):
        flag=1
        for j in range(0,i):
            if arry[j] > arry[j+1]:                     # 如果前者比后者大
                arry[j],arry[j+1] = arry[j+1],arry[j]   # 则交换两者
                flag=0
        if flag:
            break
    return arry

starttime = datetime.datetime.now()
arry=[5,4,5,7,9,3,2,3,4]
print arry
bubble_sort(arry)
print arry

endtime = datetime.datetime.now()

# 计算程序运行时间
print (endtime - starttime).seconds


#优化1：某一趟遍历如果没有数据交换,则说明已经排好序了,因此不用再进行迭代了。
#用一个标记记录这个状态即可。
def bubble_sort2(ary):
    n = len(ary)
    for i in range(n):
        flag = 1                    #标记
        for j in range(1,n-i):
            if  ary[j-1] > ary[j] :
                ary[j-1],ary[j] = ary[j],ary[j-1]
                flag = 0
        if flag :                   #全排好序了，直接跳出
            break
    return ary

arry=[5,4,5,7,9,3,2,3,4]
print arry
bubble_sort2(arry)
print arry


#优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
def bubble_sort3(ary):
    n = len(ary)
    k = n                           #k为循环的范围，初始值n
    for i in range(n):
        flag = 1
        for j in range(1,k):        #只遍历到最后交换的位置即可
            if  ary[j-1] > ary[j] :
                ary[j-1],ary[j] = ary[j],ary[j-1]
                k = j               #记录最后交换的位置
                flag = 0
        if flag :
            break
    return ary


arry=[5,4,5,7,9,3,2,3,4]
print arry
bubble_sort3(arry)
print arry