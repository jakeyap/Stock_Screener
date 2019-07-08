# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:09:59 2018

@author: Yong Keong
"""
import generate_test_data
import data_plotter
import fom_estimation as analyze
import fom_projection as predict

if True:
    data = generate_test_data.generate()
    '''
    '''
    
data_plotter.plot_full_dataset(title='testcompany old',data=data)
print('Finding stats')
stock_stats = analyze.analyze_all_data(data,showstats=True)

'''
At this point, manually look at the stats, then project data
'''

new_data = predict.modify_dataset_multi_year(data=data, predicted_stats=stock_stats, years=5)

data_plotter.plot_full_dataset(title='testcompany predictions',data=new_data)