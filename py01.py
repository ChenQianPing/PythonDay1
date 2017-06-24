#!/usr/bin/env python
# -*- coding: utf-8 -*-




"""
# 根据给定的年月日以数字形式打印出日期

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'Auguest',
    'September',
    'October',
    'November',
    'December'
]

print months

# 以1~31的娄字作为结尾的列表
endings = ['st','nd','rd'] + 17 * ['th']\
    + ['st','nd','rd'] + 7 * ['th']\
    + ['st']

print endings

year  = raw_input('Year:')
month = raw_input('Month(1-12):')
day   = raw_input('Day(1-31):')

month_number = int(month)
day_number   = int(day)

# 记得要将月份和天数减1,以获得正确的索引
month_name = months[month_number-1]
ordinal    = day + endings[day_number-1]

print month_name + '' + ordinal + ',' + year

# September18th,1981
"""


# 分片示例
# 对http://www.something.com形式的URL进行分割


print len('http://www.')   # 11
print len('.com')          # 4

url = raw_input('Please enter the URL:')


#  11: http://www.
#  -4: .com
domain = url[11:-4]
print "Domain name:" + domain



# Please enter the URL:http://www.baidu.com
# Domain name:baidu


