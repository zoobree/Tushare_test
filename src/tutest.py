# -*- coding:utf-8 -*- 

import tushare as ts 
import numpy as np

PATH = "E:/Python/Tushare/"
DATA_PATH = "E:/Python/Tushare/data/"

#df_one_stock_trade = ts.get_k_data("000651")

#df_one_stock_trade.to_csv(PATH+"000651_new.csv")

df_all_stock_basics = ts.get_stock_basics()

df_all_stock_basics.to_csv(PATH+"stock_basics.csv",encoding = 'GBK')


def decreasing_thr_judge(thr_value = 0.2, str_stock_code = "000651"):
    df_one_stock_trade = ts.get_k_data(str_stock_code)
    close_price_min = np.min(df_one_stock_trade['close'])
    close_proce_cur = df_one_stock_trade['close'].values[-1]
    print(close_proce_cur)
    print(close_price_min)
    if (close_proce_cur - close_price_min)/close_price_min < thr_value:
        return True
    else:
        return False

if __name__ == '__main__':
    df_today_all_stock = ts.get_today_all()

    array_stock_name = np.array([])
    Series_str_stock_code = df_today_all_stock['code']
    for str_stock_code in Series_str_stock_code.values:
        if decreasing_thr_judge(thr_value = 0.2, str_stock_code = str_stock_code) == True:
            np.append(array_stock_name,str_stock_code)

    with open(DATA_PATH+'decreasing_stock_name.csv', 'wb') as file_handle:
        np.savetxt(file_handle, array_stock_name, delimiter=",")