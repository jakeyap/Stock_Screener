# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:57:00 2018

0. Regex editor to grab data from Morningstar CSVs.
    Regex the following
        year
        absolute earnings
        EPS
        shares count
        Year closing share price
        Total equity
        ST debt & LT debt
        When data is found, plot the whole lot out for sanity checking

Need to extract the following
From balance sheet
1. year
2. total current assets
3. total assets
4. long term debt
5. short term debt
6. total liabilities
7. total equity

From income statement
1. Net income available to common shareholders
2. Earnings per share diluted
3. 

@author: Yong Keong
"""

import csv
import re
import matplotlib.pyplot as plt

def read_csv2data(data_directory, filename):
    ''' 
    Convert from a csv file into list of lists
    Returns:
        labels: things like year, revenue, profit etc
        datalist: a list of lists
            index 0: years
            index everything else: described by labels
    '''
    csvfile = open(data_directory+filename, 'r')
    readfile = csv.reader(csvfile)
    labels = []
    datalist = []
    counter = 0
    for eachline in readfile:
        length = len(eachline)
        print(eachline)
        if length != 1:
            # Save the labels
            labels.append(eachline[0])
            datarow = list(eachline[1:length-1])
                        
            if counter==0:
                # Strip away the trailing 12 mth '-12' string
                year_row = fmt_year_list(datarow)
                print(year_row)
                datalist.append(year_row)
            else:                
                #datarow = np.array(eachline[1:length-1])
                floatrow = [convert2float(x) for x in datarow]
                datalist.append(floatrow)
            counter = counter + 1
    return [labels,  datalist]

def convert2float(text):
    '''
    Conditional function to convert numbers into floats. 
    If it has some text, apply float function. Else return 0
    '''
    if text=='':
        return 0
    else:
        return float(text)

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