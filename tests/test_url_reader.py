# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests

url = 'http://financials.morningstar.com'+ \
    '/ajax/ReportProcess4CSV.html?t=TWTR'+ \
    '&reportType=is&period=12&dataType=A&'+ \
    'order=asc&columnYear=5&number=3'

r = requests.get(url, allow_redirects=True)
open('google.csv', 'wb').write(r.content)


mainsite = 'http://financials.morningstar.com'
query = '/ajax/ReportProcess4CSV.html?t='
company = 'BN4'
period = '&reportType=is&period=12&dataType=A&'
order = 'order=asc&columnYear=5&number=1'

url2 = mainsite+query+company+period+order
r = requests.get(url2, allow_redirects=True)

open('test.csv', 'wb').write(r.content)

def download_data(url):
    r = requests.get(url, allow_redirects=True)
    return r

def write_data2csv(data_directory, filename, data):
    open(data_directory+filename, 'wb').write(r.content)
    return

def get_income_statement_annual_url(company_code):
    header = generate_headers()
    message = '&reportType=is&period=12&dataType=A&'
    footer = generate_footers()
    url = header + company_code + message + footer
    return url

def generate_headers():
    return 'http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t='
    
def generate_footers():
    return '&dataType=A&order=asc&columnYear=5&number=1'

'''
reportType: is = Income Statement, cf = Cash Flow, bs = Balance Sheet
period: 12 for annual reporting, 3 for quarterly reporting
dataType: this doesn't seem to change and is always A
order: asc or desc (ascending or descending)
columnYear: 5 or 10 are the only two values supported
number: The units of the response data. 1 = None 2 = Thousands 3 = Millions 4 = Billions
'''