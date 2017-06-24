#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Bobby
#   E-mail  :   pingkeke@gmail.com
#   Date    :   17/6/10
#   Desc    :


import tushare as ts
from sqlalchemy import create_engine







# 大盘指数行情列表
# 获取大盘指数实时行情列表,以表格的形式展示大盘指数实时行情。

"""
返回值说明：

code:指数代码
name:指数名称
change:涨跌幅
open:开盘点位
preclose:昨日收盘点位
close:收盘点位
high:最高点位
low:最低点位
volume:成交量(手)
amount:成交金额（亿元）
"""

# df = ts.get_index()

# 获取个股以往交易历史的分笔数据明细,通过分析分笔数据,可以大致判断资金的进出情况.
# 天汽模
# df = ts.get_tick_data('002510',date='2017-06-23')

# df.head(10)

# 实时分笔
# 获取实时分笔数据,可以实时取得股票当前报价和成交信息,其中一种场景是,
# 写一个python定时程序来调用本接口（可两三秒执行一次，性能与行情软件基本一致）,
# 然后通过DataFrame的矩阵计算实现交易监控,可实时监测交易量和价格的变化。

# df = ts.get_realtime_quotes('002510') #Single stock symbol
# df[['code','name','price','bid','ask','volume','amount','time']]

# 大单交易数据
# 获取大单交易数据,默认为大于等于400手

# df = ts.get_sina_dd('002510', date='2017-06-23', vol=500)  #指定大于等于500手的数据

# 复权数据
# 默认为qfq,前复权,hfq-后复权 None-不复权
"""
返回值说明：

date : 交易日期 (index)
open : 开盘价
high : 最高价
close : 收盘价
low : 最低价
volume : 成交量
amount : 成交金额
"""
# df = ts.get_h_data('002510', start='2017-01-01', end='2017-06-23') #两个日期之间的前复权数据

# 分配预案

"""
返回值说明：

code:股票代码
name:股票名称
year:分配年份
report_date:公布日期
divi:分红金额（每10股）
shares:转增和送股数（每10股）
"""
# df = ts.profit_data(top=60)

# 行业分类
# 在现实交易中,经常会按行业统计股票的涨跌幅或资金进出,
# 本接口按照sina财经对沪深股票进行的行业分类,返回所有股票所属行业的信息.

# df = ts.get_industry_classified()

# 概念分类

# 返回股票概念的分类数据,现实的二级市场交易中,经常会以”概念”来炒作,
# 在数据分析过程中,可根据概念分类监测资金等信息的变动情况.
# 本接口是一次性在线获取数据,调用接口时会有一定的延时,请在数据返回后自行将数据进行及时存储.
# df = ts.get_concept_classified()

# 获取沪深上市公司基本情况
"""
属性包括：
code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数
"""
# df = ts.get_stock_basics()


# 存款利率
"""
返回值说明：

date :变动日期
deposit_type :存款种类
rate:利率（%）
"""
# df = ts.get_deposit_rate()

# 每日龙虎榜列表
"""
返回值说明：

code：代码
name:名称
pchange:当日涨跌幅
amount：龙虎榜成交额(万)
buy：买入额(万)
bratio：买入占总成交比例
sell：卖出额(万)
sratio：卖出占总成交比例
reason：上榜原因
date：日期
"""
# df = ts.top_list('2017-06-23')

# 数据存储
# pandas生成Json格式的文件或字符串.
# df = ts.get_hist_data('000027')
# df.to_json('/Users/chenqianping/Desktop/170409/000027.json',orient='records')

# print df
# print df[df.shares>=10]  # 选择每10股送转在10以上的;

# 实时票房
# 获取实时电影票房数据,30分钟更新一次票房数据,可随时调用.
"""
返回值说明：

BoxOffice 实时票房（万）
Irank 排名
MovieName 影片名
boxPer 票房占比 （%）
movieDay 上映天数
sumBoxOffice 累计票房（万）
time 数据获取时间
"""
# df = ts.realtime_boxoffice()

# 上证50成份股
df = ts.get_sz50s()

print df




