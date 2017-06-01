#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 运算
# http://www.runoob.com/python/python-operators.html
print "你好，世界"

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b;        # 12 = 0000 1100 ,按位与运算符,相同位的两个数字都为1,则为1;若有一个不为1,则为0.

print "Line 1 - Value of c is ", c

c = a | b;        # 61 = 0011 1101 ,按位或运算符,相同位只要一个为1即为1.
print "Line 2 - Value of c is ", c

c = a ^ b;        # 49 = 0011 0001 ,按位异或运算符,操作的结果是如果某位不同则该位为1, 否则该位为0.
print "Line 3 - Value of c is ", c

c = ~a;           # -61 = 1100 0011 ,按位取反运算符,not运算的定义是把内存中的0和1全部取反.
print "Line 4 - Value of c is ", c

c = a << 2;       # 240 = 1111 0000 ,左移动运算符
print "Line 5 - Value of c is ", c

c = a >> 2;       # 15 = 0000 1111 , 右移动运算符
print "Line 6 - Value of c is ", c