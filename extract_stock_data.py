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

mainsite = 'http://financials.morningstar.com'
query = '/ajax/ReportProcess4CSV.html?t='
company = 'BN4'
period = '&reportType=is&period=12&dataType=A&'
order = 'order=asc&columnYear=5&number=1'

url2 = mainsite+query+company+period+order
r = requests.get(url2, allow_redirects=True)
'https://morningstar-api.herokuapp.com/analysisData?ticker=GE'
data_directory = ''

open('test.csv', 'wb').write(r.content)

def download_data(url):
    '''Downloads the raw url object'''
    r = requests.get(url, allow_redirects=True)
    return r

def write_data2csv(data_directory, filename, data):
    ''' Writes the object into a csv file. Return a matrix '''
    '''NOT DONE YET'''
    open(data_directory+filename, 'wb').write(r.content)
    return

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