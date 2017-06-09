#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 翻译一下:假如你有3张1元,3张5元,3张10元,假设买东西不允许补钱,请问你最大的不可支付的费用是多少元？( Bobby原创题  答案是:44元)
# 每样3张,3*6+3*7+3*8= 48

# print(3*1+3*5+3*10)  # 48

a = 1
b = 5
c = 10
t = 3      # 票的张数,假设1、5、10各有3张（3张够了）,先计算出所有的可能组合
s = []     # 排列组合全部放到这里
# 生成的组合
for i in range(t+1):  # 代表从0到t+1(不包含t+1);
    s1 = a*i
    s.append(s1)
    for j in range(t+1):
        s2 = a*i+b*j
        s.append(s2)
        for k in range(t+1):
            s3 = a*i + b*j + c*k
            s.append(s3)


print(s)

# 排序
s.sort()

# 去掉重复
news = []
for i in s:
    if i not in news:
        news.append(i)
print("组合生成的最大数%s"%news[-1])

print("组合排序后列表%s"%news)

# 提取不在列表中的数字
r = []
for i in range((a+b+c)*t):
    if i in news:
        pass
    else:
        r.append(i)
print("组合不能生成的数字%s"%r)
print("不能生成的最大数字为%s"%r[-1])

