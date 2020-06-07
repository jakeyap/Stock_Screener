# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:57:00 2018

    dictionary names
    'year':year, 
    'roe':roe,
    'fcfps':fcfps,
    'eps':eps,
    'dividend':dividend,
    'payout_ratio':payout_ratio,
    'bookvalue':bookvalue,
    'numberofshares':numberofshares,
    'pe_ratio':pe_ratio
    'pb_ratio':pb_ratio
    'leverage_ratio':leverage_ratio
@author: Yong Keong
"""

import csv
import re
import matplotlib.pyplot as plt

def read_csv2data(data_directory, filename):
    ''' 
    Convert from a csv file into dictionary of data
    Arguments: data_directory, filename, self explanatory
    Returns:
       data: a dictionary
          {'year': list of years
          'eps': list of eps
          'dividend': list of dividends
          'payout_ratio': list of payout ratios
          'numberofshares': list of sharecount
          'bookvalue': list of book value
          'fcfps': list of fcfps
          'roe': list of roe
          'pe_ratio': list of pe
          'pb_ratio': list of pb
          'leverage_ratio':leverage_ratio
          }
     '''
    csvfile = open(data_directory+filename, 'r')
    readfile = csv.reader(csvfile)
    
    data = {}
   
    counter = 0
    for eachline in readfile:
        # Grab data without TTM
        # this is year
        # Strip away the trailing 12 mth '-12' string
        if (counter == 0):
            data['year'] = fmt_year_list(list(eachline[1:-1]))
        elif (counter==1): # this is EPS
            data['eps'] = convert2float_list(list(eachline[1:-1]))
        elif (counter==2): # this is dividend
            data['dividend'] = convert2float_list(list(eachline[1:-1]))
        elif (counter==3): # this is payout_ratio
            data['payout_ratio'] = convert2float_list(list(eachline[1:-1]))
        elif (counter==4): # this is numberofshares
            data['numberofshares'] = convert2float_list(list(eachline[1:-1]))
        elif (counter==5): # this is bookvalue
            data['bookvalue'] = convert2float_list(list(eachline[1:-1]))
        elif (counter==6): # this is fcfps
            data['fcfps'] = convert2float_list(list(eachline[1:-1]))
        elif (counter==7): # this is roe
            data['roe'] = convert2float_list(list(eachline[1:-1]))
        elif (counter==8): # this is pe_ratio
            data['pe_ratio'] = convert2float_list(list(eachline[1:-1]))
        elif (counter==9): # this is pb_ratio
            data['pb_ratio'] = convert2float_list(list(eachline[1:-1]))
        elif (counter==10): # this is financial leverage ratio
            data['leverage_ratio'] = convert2float_list(list(eachline[1:-1]))
        else:
            pass
        counter = counter + 1
    return data


def convert2float_list(stringlist):
    '''
    Function to convert list of strings into floats
    '''
    newlist = []
    for each in stringlist:
        newlist.append(convert2float(each))
    return newlist

def convert2float(text):
    '''
    Conditional function to convert numbers into floats. 
    If it has some text, apply float function. Else return 0
    '''
    try:
        return float(text)
    except Exception:
        return 0

def fmt_year_list(yearlist):
    ''' 
    The morningstar years may have a -12 appended to mean december
    Remove it. This is for handling a list of years
    '''
    newlist = []
    for eachyear in yearlist:
        newlist.append(fmt_year(eachyear))
    return newlist

def fmt_year(year_string):
    ''' 
    The morningstar years may have a -12 appended to mean december
    Remove it.
    '''
    year = re.split('-', year_string)
    year = int(year[0])
    return year

def plot_all_is(labels, year, raw_data):
    counter = 0
    plt.subplot(5,4,1)
    for eachlabel in labels[1:]:
        plt.subplot(5,4,20-counter)
        plt.plot(year, raw_data[counter], marker='x')
        plt.title(eachlabel,size=6)
        plt.grid(True)
        ''' Get the ylimit, then scale it from 0 to such'''
        limits = plt.ylim()
        if limits[0]<0 and limits[1]<0:
            newlimit = [1.2*limits[0], 0]
        elif limits[0]>0 and limits[1]>0:
            newlimit = [0, limits[1]*1.2]
        else:
            newlimit = [1.2*limits[0], limits[1]*1.2]
        plt.ylim(newlimit)
        axes = plt.gca()
        axes.set_xticks(year)
        axes.set_xticklabels([])
        counter = counter + 1
    for each in [17,18,19,20]:
        plt.subplot(5,4,each)
        axes = plt.gca()
        axes.set_xticklabels(year, rotation = 45)
        
if __name__=='__main__':
    directory = 'sample_data/'
    filename = 'Google_2019_condensed.csv'
    data = read_csv2data(directory, filename)