# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:57:00 2018

URL reading from morningstar seems a little buggy. 
Cannot get 10 year data
But just go ahead anyway. Signed up for API trial 

0. Regex editor to grab data from Morningstar.
    Download the financial statements first (optional)
    Regex the following
        year
        absolute earnings
        EPS
        shares count
        Year closing share price
        Total equity
        Retained earnings
        ST debt & LT debt
        When data is found, plot the whole lot out for sanity checking


@author: Yong Keong
"""

import requests
import numpy as np
import csv
import re
import matplotlib.pyplot as plt

def download_data(url):
    '''Downloads the raw url object'''
    r = requests.get(url, allow_redirects=True)
    return r

def write_data2csv(data_directory, filename, data):
    ''' Writes the object into a csv file. '''
    open(data_directory+filename, 'wb').write(data.content)    
    return

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
                floatrow = [float(x) for x in datarow]
                datalist.append(floatrow)
            counter = counter + 1
    return [labels,  datalist]

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

def plot_all(labels, year, raw_data):
    counter = 0
    plt.subplot(5,4,1)
    for eachlabel in labels[1:]:
        plt.subplot(5,4,1+counter)
        plt.plot(year, raw_data[counter], marker='x')
        plt.title(eachlabel,size=6)
        plt.grid(True)
        ''' Get the ylimit, then scale it from 0 to such'''
        limits = plt.ylim()
        if limits[0]<0:
            newlimit = [-limits[0]*1.2, limits[1]*1.2]
        else:
            newlimit = [0, limits[1]*1.2]
        plt.ylim(newlimit)
        axes = plt.gca()
        axes.set_xticks(year)
        axes.set_xticklabels([])
        counter = counter + 1
    for each in [17,18,19,20]:
        plt.subplot(5,4,each)
        axes = plt.gca()
        axes.set_xticklabels(year, rotation = 45)

def get_income_statement_annual_url(company_code):
    '''Generates the required files to get the necessary financial docs'''
    [header,footer] = generate_url_skeleton()
    message = '&reportType=is&period=12&dataType=A&'
    url = header + company_code + message + footer
    return url

def get_income_statement_quarter_url(company_code):
    '''Generates the required files to get the necessary financial docs'''
    [header,footer] = generate_url_skeleton()
    message = '&reportType=is&period=3&dataType=A&'
    url = header + company_code + message + footer
    return url

def get_balance_sheet_annual_url(company_code):
    '''Generates the required files to get the necessary financial docs'''
    [header,footer] = generate_url_skeleton()
    message = '&reportType=bs&period=12&dataType=A&'
    url = header + company_code + message + footer
    return url

def get_balance_sheet_quarter_url(company_code):
    '''Generates the required files to get the necessary financial docs'''
    [header,footer] = generate_url_skeleton()
    message = '&reportType=bs&period=3&dataType=A&'
    url = header + company_code + message + footer
    return url

def get_cashflow_annual_url(company_code):
    '''Generates the required files to get the necessary financial docs'''
    [header,footer] = generate_url_skeleton()
    message = '&reportType=cf&period=12&dataType=A&'
    url = header + company_code + message + footer
    return url

def get_cashflow_quarter_url(company_code):
    '''Generates the required files to get the necessary financial docs'''
    [header,footer] = generate_url_skeleton()
    message = '&reportType=cf&period=3&dataType=A&'
    url = header + company_code + message + footer
    return url

def generate_url_skeleton():
    '''Generates the header and footers for the csv url'''
    header = 'http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t='
    footer = '&dataType=A&order=asc&columnYear=5&number=1'
    return [header, footer]
    

'''
reportType: is = Income Statement, cf = Cash Flow, bs = Balance Sheet
period: 12 for annual reporting, 3 for quarterly reporting
dataType: this doesn't seem to change and is always A. R is restated
order: asc or desc (ascending or descending)
columnYear: 5 or 10 are the only two values supported
number: The units of the response data. 1 = None 2 = Thousands 3 = Millions 4 = Billions
'''