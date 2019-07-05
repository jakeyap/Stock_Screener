# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:09:59 2018

@author: Yong Keong
"""
import generate_test_data
import data_plotter

if True:
    data = generate_test_data.generate()
    

'''
counter = 1
while counter < length:
    title = listofparams[counter]
    data = listoflists[counter]
    data_plotter.plot_data(year,data,title,'')
    counter = counter + 1
'''

data_plotter.plot_full_dataset(data)