#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

print("Demo05")

# 交换两个变量值
#---------------------------------------
a = 3
b = 22

print(a)
print(b)


a,b = b,a

print(a)
print(b)


# 去掉list中的重复元素
#---------------------------------------

old_list = [1,1,1,3,4]

print(old_list)

new_list = list(set(old_list))
print(new_list)

L1 = [4,1,3,2,3,5,1]
print L1
L2 = []
[L2.append(i) for i in L1 if i not in L2]
print L2



# 翻转一个字符串
#---------------------------------------
s = 'abcde'
print(s)
ss = s[::-1]
print(ss)


# 用两个元素之间有对应关系的list构造一个dict
#---------------------------------------
names = ['jianpx', 'yue']
ages = [23, 40]
m = dict(zip(names,ages))
print(m)


#将数量较多的字符串相连,如何效率较高,为什么
#---------------------------------------
fruits = ['apple', ' banana']
result = ''.join(fruits)
print (result)

"""python字符串效率问题之一就是在连接字符串的时候使用‘+’号，
例如 s = ‘s1’ + ‘s2’ + ‘s3’ + ...+’sN’，总共将N个字符串连接起来， 
但是使用+号的话，python需要申请N-1次内存空间， 
然后进行字符串拷贝。
原因是字符串对象PyStringObject在python当中是不可变对象，
所以每当需要合并两个字符串的时候，
就要重新申请一个新的内存空间 （大小为两个字符串长度之和）来给这个合并之后的新字符串，然后进行拷贝。 
所以用+号效率非常低。

* 建议在连接字符串的时候使用字符串本身的方法 join（list），这个方法能提高效率，原因是它只是申请了一次内存空间，
 因为它可以遍历list中的元素计算出总共需要申请的内存空间的大小，一次申请完。
"""

# 用Python生成指定长度的斐波那契数列
#---------------------------------------

def fibs(x):
    result = [0, 1]
    for index in range(x - 2):
        result.append(result[-2] + result[-1])
    return result

"""
if __name__ == '__main__':
    num = input('Enter one number: ')
    print fibs(num)
"""

# Python里如何生产随机数
# import random
#---------------------------------------

print(random.randint(1,11))
print(random.choice(range(11)))


# Python是如何进行类型转换的
print(int('1234'))  # 将数字型字符串转为整形  1234
print(float(12))    # 将整形或数字字符转为浮点型  12.0
print(str(98))      # 将其他类型转为字符串型  98
print(list('abcd')) # 将其他类型转为列表类型  ['a', 'b', 'c', 'd']
print(dict.fromkeys(['name','age'])) # 将其他类型转为字典类型  {'age': None, 'name': None}
print(tuple([1, 2, 3, 4]) )          # 将其他类型转为元祖类型  (1, 2, 3, 4)

"""
详细转换总结如下:

函数                         描述  
int(x [,base])              将x转换为一个整数  
long(x [,base] )            将x转换为一个长整数  
float(x)                    将x转换到一个浮点数  
complex(real [,imag])       创建一个复数  
str(x)                      将对象 x 转换为字符串  
repr(x)                     将对象 x 转换为表达式字符串  
eval(str)                   用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s)                    将序列 s 转换为一个元组  
list(s)                     将序列 s 转换为一个列表  
set(s)                      转换为可变集合  
dict(d)                     创建一个字典。d 必须是一个序列 (key,value)元组。  
frozenset(s)                转换为不可变集合  
chr(x)                      将一个整数转换为一个字符  
unichr(x)                   将一个整数转换为Unicode字符  
ord(x)                      将一个字符转换为它的整数值  
hex(x)                      将一个整数转换为一个十六进制字符串  
oct(x)                      将一个整数转换为一个八进制字符串  

"""

