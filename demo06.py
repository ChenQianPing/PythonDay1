#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random    #这个是注释,引入模块
import turtle
import time

# rnd = random.randint(1,500)  #生成1-500之间的随机数

# print rnd


turtle.pensize(2)
turtle.bgcolor("black")
colors =["red","yellow","purple","blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
    turtle.tracer(True)

"""
发现了一段比较有趣的Python…好吧其实也不算很有趣,
就是一个绘图程序,但只有短短几行,有兴趣的同学可以拿去研究一下哟
"""