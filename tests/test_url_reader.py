# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import extract_stock_data as ms
import matplotlib.pyplot as plt

company = 'BN4'

bs_url = ms.get_balance_sheet_annual_url(company)
bs_data = ms.download_data(bs_url)

is_url = ms.get_income_statement_annual_url(company)
is_data = ms.download_data(is_url)

cf_url = ms.get_cashflow_annual_url(company)
cf_data = ms.download_data(cf_url)

ms.write_data2csv('','BN4_bs_2018.csv', bs_data)
ms.write_data2csv('','BN4_is_2018.csv', is_data)
ms.write_data2csv('','BN4_cf_2018.csv', cf_data)

#raw_bs_data = ms.read_csv2data('','BN4_bs_2018.csv')
"""
bs_labels = raw_bs_data[0]
bs_data = raw_bs_data[1]

length = len(bs_labels)
year = bs_data[0]
samplemetric = bs_data[1]
ms.plot_all(bs_labels,year,bs_data[1:])

#year0 = ms.format_year(year[0])
"""
