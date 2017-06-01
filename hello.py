#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 被注释内容
""" 被注释内容 """

import sys
import getpass

print "你好，世界"

print sys.argv

print "hello,world"

# 声明变量,上述代码声明了一个变量,变量名为:name,变量name的值为:"Bobby"
# 变量的作用:昵称,其代指内存里某个地址中保存的内容


""" 变量定义的规则：
变量名只能是 字母、数字或下划线的任意组合;
变量名的第一个字符不能是数字;
关键字不能声明为变量名;
 """

name1 = "Bobby"
name2 = name1

print name2

# 流程控制和缩进
# 提示输入用户名和密码

# 验证用户名和密码
#     如果错误,则输出用户名或密码错误
#     如果成功,则输出 欢迎,XXX!


name = raw_input('请输入用户名：')
# pwd = getpass.getpass('请输入密码:')
pwd = getpass.getpass(prompt='请输入密码:\n')

if name == "Bobby" and pwd == "cmd":
    print "欢迎,Bobby！"
else:
    print "用户名和密码错误"


# 根据用户输入内容打印其权限

# alex --> 超级管理员
# eric --> 普通管理员
# tony --> 业务主管
# 其他 --> 普通用户

name = raw_input('请输入用户名：')

if name == "alex":
    print "超级管理员"
elif name == "eric":
    print "普通管理员"
elif name == "tony":
    print "业务主管"
else:
    print "普通用户"

""" python中的字符串在C语言中体现为是一个字符数组,每次创建字符串时候需要在内存中开辟一块连续的空，
并且一旦需要修改字符串的话，就需要再次开辟空间，万恶的+号每出现一次就会在内从中重新开辟一块空间。 """

name = "alex"

print "i am %s " % name

# 创建列表 name_list ＝ list(['alex', 'seven', 'eric'])
name_list = ['alex', 'seven', 'eric']

print name_list

# 创建元祖 ages = (11, 22, 33, 44, 55)
ages = tuple((11, 22, 33, 44, 55))

print ages

# 创建字典 person = dict({"name": "mr.wu", 'age': 18})
person = {"name": "mr.wu", 'age': 18}

print person


# pyCharm最新2017激活码 http://blog.csdn.net/fx677588/article/details/58164902
# Python之路【第一篇】：Python简介和入门 http://www.cnblogs.com/wupeiqi/articles/4906230.html