# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:09:59 2018

@author: Yong Keong
"""
import generate_test_data
import data_plotter as plotter
import fom_estimation as analyser
import fom_projection as predictor
import extract_stock_data as extractor

estimated_roe = 15
estimated_pe = 25
dcf_rate = 10
currentyear = 2019

fakedata = False

if fakedata:
   data = generate_test_data.generate()
else:
   directory = 'sample_data/'
   filename = 'Google_2019_condensed.csv'
   data = extractor.read_csv2data(directory, filename)

directory = directory + 'generated_plots/'
plotter.plot_full_dataset(title='testcompany old',data=data,directory=directory)
print('Finding stats')
stock_stats = analyser.analyze_all_data(data,showstats=True)

'''
At this point, manually look at the stats, then tune ROE, payoutratio, PE to imagine scenarios project data
need to calculate the DCF into today
'''

stock_stats['roe_avg'] = estimated_roe
stock_stats['pe_ratio_avg'] = estimated_pe
# stock_stats['payout_ratio_avg'] = 
new_data = predictor.modify_dataset_multi_year(data=data, predicted_stats=stock_stats, years=10)
plotter.plot_full_dataset(title='Google predictions',data=new_data, directory=directory, projectionyear=2019)

print('Long term ROE: ' + str(estimated_roe))
print('Estimated PE:  ' + str(estimated_pe))
print('Discount rate: ' + str(dcf_rate) + '%')

print('Estimated present value:')
print(predictor.dcf_calculator(year=currentyear,
                               data=new_data,
                               discount_rate=dcf_rate))