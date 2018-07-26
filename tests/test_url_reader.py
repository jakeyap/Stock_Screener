# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import extract_stock_data as ms
import matplotlib.pyplot as plt

company = 'BN4'

# url = ms.get_balance_sheet_annual_url(company)
# data_raw = ms.download_data(url)
# ms.write_data2csv('','BN4_bs_2018.csv', data_raw)
raw_data = ms.read_csv2data('','BN4_bs_2018.csv')

labels = raw_data[0]
data = raw_data[1]

length = len(labels)
year = data[0]
year.toarray()
samplemetric = data[1]

#plt.plot(year,samplemetric)

year0 = ms.format_year(year[0])