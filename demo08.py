#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
小王，小李，小张和小周4个人共为某希望小学捐赠了25个书包，
按照数量多少的顺序分别是小王，小李，小张，小周。
已知小王捐赠的书包数量是小李和小张捐赠书包数量之和；
小李捐赠的书包数量是小张和小周捐赠的书包数量之和。
问小王捐赠了多少个书包？

x1+x2+x3+x4=25;
x1>x2>x3>x4;
x1=x2+x3;
x2=x3+x4;
求X1?   11;

"""

__author__ = 'Bobby'
__date__ = '2017-06-09'

# 解法1:
for wang in range(26):  # 代表从0到26(不包含26);
    for li in range(26):
        for zhang in range(26):
            for zhou in range(26):
                if wang + li + zhang + zhou == 25 and wang > li > zhang > zhou and wang == li + zhang and li == zhang + zhou:
                    print wang
                else:
                    continue


# 解法2:
for zhou in range(5):  # 小周
	    for zhang in range(8):  # 小张
		        if 3*zhou +4*zhang==25:
			            print 2*zhang+zhou, zhou+zhang, zhang, zhou
			            break