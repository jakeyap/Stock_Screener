# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import extract_stock_data as ms
import data_scrapper as downloader
import matplotlib.pyplot as plt
import time

company = 'BN4'
year = '_2018'

bs_url = downloader.get_balance_sheet_annual_url(company)
raw_bs_data = downloader.download_data(bs_url)

is_url = downloader.get_income_statement_annual_url(company)
raw_is_data = downloader.download_data(is_url)

cf_url = downloader.get_cashflow_annual_url(company)
raw_cf_data = downloader.download_data(cf_url)

downloader.write_data2csv('',company+year+'_bs.csv', raw_bs_data)
time.sleep(1)
#downloader.write_data2csv('',company+year+'_is.csv', raw_is_data)
#time.sleep(1)
#downloader.write_data2csv('',company+year+'_cf.csv', raw_cf_data)

#bs_data = ms.read_csv2data('',company+year+'_bs.csv')
#is_data = ms.read_csv2data('',company+year+'_is.csv')
'''
is_labels = is_data[0]
is_data = is_data[1]

length = len(is_labels)
year = is_data[0]
samplemetric = is_data[1]
ms.plot_all_is(is_labels,year,is_data[1:])

#year0 = ms.format_year(year[0])
'''