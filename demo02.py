#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 面向对象（初级篇）

# 封装示例

# 创建类
class Foo:
    def Bar(self):
        print 'Bar'

    def Hello(self, name):
        print 'i am %s' % name


# 根据类Foo创建对象obj
obj = Foo()
obj.Bar()  # 执行Bar方法
obj.Hello('Bobby')  # 执行Hello方法　


class Foo:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def kanchai(self):
        print "%s,%s岁,%s,上山去砍柴" % (self.name, self.age, self.gender)

    def qudongbei(self):
        print "%s,%s岁,%s,开车去东北" % (self.name, self.age, self.gender)

    def dabaojian(self):
        print "%s,%s岁,%s,最爱大保健" % (self.name, self.age, self.gender)


xiaoming = Foo('小明', 10, '男')
xiaoming.kanchai()
xiaoming.qudongbei()
xiaoming.dabaojian()

laoli = Foo('老李', 90, '男')
laoli.kanchai()
laoli.qudongbei()
laoli.dabaojian()


# #####################  定义实现功能的类  #####################

class Person:
    def __init__(self, na, gen, age, fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight = fig

    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""

        self.fight = self.fight - 200

    def practice(self):
        """注释：自我修炼，增长100战斗力"""

        self.fight = self.fight + 200

    def incest(self):
        """注释：多人游戏，消耗500战斗力"""

        self.fight = self.fight - 500

    def detail(self):
        """注释：当前对象的详细情况"""

        temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s" % (self.name, self.gender, self.age, self.fight)
        print temp


# #####################  开始游戏  #####################

cang = Person('苍井井', '女', 18, 1000)    # 创建苍井井角色
dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
bo = Person('波多多', '女', 19, 2500)      # 创建波多多角色

cang.incest()   # 苍井空参加一次多人游戏
dong.practice()  # 东尼木木自我修炼了一次
bo.grassland()  # 波多多参加一次草丛战斗

# 输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()

cang.incest()  # 苍井空又参加一次多人游戏
dong.incest()  # 东尼木木也参加了一个多人游戏
bo.practice()  # 波多多自我修炼了一次

# 输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()


# 继承示例

# Python的类可以继承多个类,Java和C#中则只能继承一个类;
# Python的类如果继承了多个类,那么其寻找方法的方式有两种,分别是:深度优先和广度优先;

class Animal:
    def eat(self):
        print "%s 吃 " % self.name

    def drink(self):
        print "%s 喝 " % self.name

    def shit(self):
        print "%s 拉 " % self.name

    def pee(self):
        print "%s 撒 " % self.name


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print '喵喵叫'


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print '汪汪叫'


# ######### 执行 #########

c1 = Cat('小白家的小黑猫')
c1.eat()

c2 = Cat('小黑的小白猫')
c2.cry()

d1 = Dog('胖子家的小瘦狗')
d1.cry()



class D:

    def bar(self):
        print 'D.bar'


class C(D):

    def bar(self):
        print 'C.bar'


class B(D):

    def bar(self):
        print 'B.bar'


class A(B, C):

    def bar(self):
        print 'A.bar'

a = A()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去D类中找，如果D类中么有，则继续去C类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> D --> C
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()


class D(object):

    def bar(self):
        print 'D.bar'


class C(D):

    def bar(self):
        print 'C.bar'


class B(D):

    def bar(self):
        print 'B.bar'


class A(B, C):

    def bar(self):
        print 'A.bar'

a = A()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> C --> D
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()

""" 经典类：首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去D类中找，如果D类中么有，
则继续去C类中找，如果还是未找到，则报错 

新式类：首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，
如果还是未找到，则报错

注意：在上述查找过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
"""


# 多态
# Pyhon不支持Java和C#这一类强类型语言中多态的写法，但是原生多态，其Python崇尚“鸭子类型”。

class F1:
    pass


class S1(F1):

    def show(self):
        print 'S1.show'


class S2(F1):

    def show(self):
        print 'S2.show'

def Func(obj):
    print obj.show()

s1_obj = S1()
Func(s1_obj)

s2_obj = S2()
Func(s2_obj)


""" 
一般在Python开发中，全部使用面向对象或面向对象和函数式混合使用;
http://www.cnblogs.com/wupeiqi/p/4493506.html

"""
