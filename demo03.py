#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 面向对象（进阶篇）

class Province:

    # 静态字段
    country = '中国'

    def __init__(self, name):

        # 普通字段
        self.name = name


# 直接访问普通字段
obj = Province('河北省')
print obj.name

# 直接访问静态字段
print(Province.country)

"""
# 字段
包括：普通字段和静态字段,他们在定义和使用中有所区别,而最本质的区别是内存中保存的位置不同,
* 普通字段属于对象,普通字段在每个对象中都要保存一份;
* 静态字段属于类,静态字段在内存中只保存一份;

应用场景:通过类创建对象时,如果每个对象都具有相同的字段,那么就使用静态字段.
"""


class Foo:

    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义普通方法,至少有一个self参数 """

        # print self.name
        print '普通方法'

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """

        print '类方法'

    @staticmethod
    def static_func():
        """ 定义静态方法 ,无默认参数"""

        print '静态方法'


# 调用普通方法
f = Foo("name")
f.ord_func()

# 调用类方法
Foo.class_func()

# 调用静态方法
Foo.static_func()

"""
# 方法
包括：普通方法、静态方法和类方法,三种方法在内存中都归属于类,区别在于调用方式不同.
* 普通方法：由对象调用;至少一个self参数;执行普通方法时,自动将调用该方法的对象赋值给self；
* 类方法：由类调用; 至少一个cls参数;执行类方法时,自动将调用该方法的类复制给cls;
* 静态方法：由类调用;无默认参数;

相同点:对于所有的方法而言，均属于类（非对象）中,所以,在内存中也只保存一份.
不同点:方法调用者不同、调用方法时自动传入的参数不同.
"""


# ############### 定义 ###############
class Foo2:

    def func(self):
        pass

    # 定义属性
    @property
    def prop(self):
        pass
# ############### 调用 ###############
foo_obj = Foo2()

foo_obj.func()
foo_obj.prop   #调用属性

"""
实例：对于主机列表页面，每次请求不可能把数据库中的所有内容都显示到页面上，而是通过分页的功能局部显示，
所以在向数据库中请求数据时就要显示的指定获取从第m条到第n条的所有数据（即：limit m,n），这个分页的功能包括：

根据用户请求的当前页和总数据条数计算出 m 和 n
根据m 和 n 去数据库中请求数据 
"""


# ############### 定义 ###############
class Pager:
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


# ############### 调用 ###############

p = Pager(2)
print(p.start)   # 就是起始值，即:m  10
print(p.end)     # 就是结束值，即:n  20



# 经典类,具有一种@property装饰器
# ############### 定义 ###############
class Goods:

    @property
    def price(self):
        return "Bobby"
# ############### 调用 ###############
obj = Goods()
result = obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
print(result)


"""
# 新式类,具有三种@property装饰器

# ############### 定义 ###############
class Goods(object):

    @property
    def price(self):
        print '@property'

    @price.setter
    def price(self, value):
        print '@price.setter'

    @price.deleter
    def price(self):
        print '@price.deleter'

# ############### 调用 ###############
obj = Goods()

obj.price          # 自动执行 @property 修饰的 price 方法，并获取方法的返回值

obj.price = 123    # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数

del obj.price      # 自动执行 @price.deleter 修饰的 price 方法
"""

# 由于新式类中具有三种访问方式，我们可以根据他们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除

class Goods01(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods01()
print(obj.price)         # 获取商品价格
obj.price = 200          # 修改商品原价
print(obj.price)
del obj.price            # 删除商品原价


class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, '价格属性描述...')

obj = Goods()
obj.PRICE         # 获取商品价格
print(obj.PRICE)
obj.PRICE = 200   # 修改商品原价
print(obj.PRICE)
del obj.PRICE     # 删除商品原价


class Foo:

    def get_bar(self):
        return 'get_bar'

    # *必须两个参数
    def set_bar(self, value):
        return 'set value' + value

    def del_bar(self):
        return 'del_bar'

    BAR = property(get_bar, set_bar, del_bar, 'description...')

obj = Foo()

print(obj.BAR)       # 自动调用第一个参数中定义的方法：get_bar
obj.BAR = "alex"     # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
print(obj.BAR)
del Foo.BAR          # 自动调用第三个参数中定义的方法：del_bar方法
print(obj.BAR)
obj.BAR              # 自动获取第四个参数中设置的值：description...
print(obj.__doc__)



