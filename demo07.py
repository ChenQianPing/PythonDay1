#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division  # 导入实除法模块后的结果为浮点数
# http://blog.csdn.net/kong_90/article/details/45956011
# 根据题意排列组合总共的情况有387420489种,符合等式的情况有3359844种,在总情况中占0.008672.
"""
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            for l in range(1,10):
                for m in range(1,10):
                    for n in range(1,10):
                        for o in range(1,10):
                            for p in range(1,10):
                                for q in range(1,10):
                                    if(i+13*j/k+l+12*m-n-11+o*p/q-10==66):
                                        print i,j,k,l,m,n,o,p,q
"""



print 3359844/387420489  #0.00867234463689