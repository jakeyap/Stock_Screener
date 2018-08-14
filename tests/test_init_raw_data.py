# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:26:48 2018

@author: Yong Keong
"""
import csv
import curve_fitting_functions as fit
import numpy as np

directory = '../sample_data/'
filename_yzj = 'BS6_2018.csv'
filename_keppel = 'BN4_2018.csv'
filename_visa = 'V_2018.csv'

file_yzj = open((directory + filename_yzj), 'r')
file_keppel = open((directory + filename_keppel), 'r')
file_visa = open((directory + filename_visa), 'r')

csv_yzj = csv.reader(file_yzj, delimiter=',')
csv_keppel = csv.reader(file_keppel, delimiter=',')
csv_visa = csv.reader(file_visa, delimiter=',')

data_yzj = []
data_keppel = []
data_visa = []
"""
for eachline in csv_yzj:
    temp_list = []    
    for each_element in eachline:
        temp_list.append(each_element)
    data_yzj.append(temp_list)

for eachline in csv_keppel:
    temp_list = []
    for each_element in eachline:
        temp_list.append(each_element)
    data_keppel.append(temp_list)
    
for eachline in csv_visa:
    temp_list = []
    for each_element in eachline:
        temp_list.append(each_element)
    data_visa.append(temp_list)
"""

for eachline in csv_visa:
    temp_list = []
    for each_element in eachline:
        temp_list.append(each_element)
    data_visa.append(temp_list)
    
# Done. Sample data will be initialized
data_visa = [[item.replace(',','') for item in line] for line in data_visa]

year_visa= list(map(int,data_visa[0][2:]))
eps_visa = list(map(float,data_visa[2][2:]))
bvps_visa = list(map(float,data_visa[3][2:]))
fcfps_visa= list(map(float,data_visa[4][2:]))
div_visa  = list(map(float,data_visa[5][2:]))
shares_visa=list(map(float,data_visa[6][2:]))
eq_percent_visa = list(map(float,data_visa[9][2:]))
st_percent_visa = list(map(float,data_visa[10][2:]))
lt_percent_visa = list(map(float,data_visa[11][2:]))
stockprice_visa = list(map(float,data_visa[12][2:]))

#year_yzj = np.subtract(year_yzj,year_yzj[0]-1).tolist()
visa_proj_data = fit.create_projections(year_visa,eps_visa,5)
'''
Outputs:
    [
    proj_year_arr: real and projected years
    y_vals_exp: exponential fit
    y_vals_lin: linear fit
    y_vals_log: log fit
    exp_label: label to put on the graph
    lin_label: label to put on the graph
    log_label: label to put on the graph
    ]
'''
fit.plot_earnings(year_visa, eps_visa, visa_proj_data, 'VISA EPS')
