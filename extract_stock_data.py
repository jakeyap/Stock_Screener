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

def download_data(url):
    '''Downloads the raw url object'''
    r = requests.get(url, allow_redirects=True)
    return r

def write_data2csv(data_directory, filename, data):
    ''' Writes the object into a csv file. '''
    open(data_directory+filename, 'wb').write(data.content)    
    return

def read_csv2data(data_directory, filename):
    ''' Convert from a csv file into matrix '''
    csvfile = open(data_directory+filename, 'r')
    readfile = csv.reader(csvfile)
    labels = []
    datalist = []
    
    for eachline in readfile:
        length = len(eachline)
        if length != 1:
            # Save the labels
            labels.append(eachline[0])
            # Strip away the trailing 12 mth data
            ''' TO DO: Format the dates and numbers properly'''
            datarow = np.array(eachline[1:length-1])
            datalist.append(datarow)
        data = np.matrix(datalist)
    return [labels, data]

def remove_dash(string):
    ''' 
    The morningstar years may have a -12 appended to mean december
    Remove it
    '''
    year = re.split('-', string)
    year = int(year[0])
    return year

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