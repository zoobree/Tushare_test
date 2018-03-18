# -*- coding:utf-8 -*- 

import tushare as ts

PATH = "E:/Python/Tushare/"

#df_one_stock_trade = ts.get_k_data("000651")

#df_one_stock_trade.to_csv(PATH+"000651_new.csv")

df_all_stock_basics = ts.get_stock_basics()

df_all_stock_basics.to_csv(PATH+"stock_basics.csv",encoding = 'GBK')


def get_decreasing_stocks(thr_value,str_stock_code="000651"):
    df_one_stock_trade = ts.get_k_data(str_stock_code)

