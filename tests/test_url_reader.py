# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import extract_stock_data as ms
import data_scrapper as downloader
import matplotlib.pyplot as plt
import time

company = 'BS6'
year = '_2018'
"""
bs_url = downloader.get_balance_sheet_annual_url(company)
raw_bs_data = downloader.download_data(bs_url)

is_url = downloader.get_income_statement_annual_url(company)
raw_is_data = downloader.download_data(is_url)

cf_url = downloader.get_cashflow_annual_url(company)
raw_cf_data = downloader.download_data(cf_url)
downloader.write_data2csv('',company+year+'_bs.csv', raw_bs_data)
time.sleep(1)
"""

url = downloader.get_key_results_url(company)
rawdata = downloader.download_data(url)
downloader.write_data2csv('',company+year+'_kr.csv',rawdata)


'''
is_labels = is_data[0]
is_data = is_data[1]

length = len(is_labels)
year = is_data[0]
samplemetric = is_data[1]
ms.plot_all_is(is_labels,year,is_data[1:])

#year0 = ms.format_year(year[0])
'''
