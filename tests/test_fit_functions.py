# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:57:31 2018
File under test:
    curve_fitting_functions.py
    

@author: Yong Keong
"""
import curve_fitting_functions as fitting

earnings = [4.05e9, 4.45e9,4.24e9,4.37e9]
year0 = [1,2,3,4]
year1 = [2014,2015,2016,2017]

# Switch between real years & indexed from 0 years to test data
year = year1

proj_data = fitting.create_projections(year,earnings,10)
fitting.plot_earnings(year,earnings,proj_data,'Test')
