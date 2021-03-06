# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:33:57 2018

@author: Yong Keong
"""

def generate():
   '''
   listofparams = ['year', 
                   'return on equity', 
                   'free cashflow per share',
                   'earnings per share', 
                   'dividends per share',
                   'payout ratio', 
                   'book value per share',
                   'number of shares',
                   'price-earnings ratio']
   '''
    
   year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
   roe = [7.19, 10.6, 12.31, 14.19, 7.91, 18.21, 19.97, 22.05, 20.79, 23.76, 34.14]
   fcfps = [0, 0.08, 0.83, 1.24, 1.5, 0.72, 2.75, 2.49, 1.8, 3.42, 0]
   eps = [0.24,0.78,1,1.29,0.79,1.9,2.16,2.58,2.48,2.8,4.09]
   dividend = [0.03,0.1,0.13,0.15,0.22,0.33,0.4,0.48,0.56,0.66,0.78]
   payout_ratio = [0,13.6,12.5,11.6,40.9,14.7,17.5,19.2,23.4,23.6,19.1]
   bookvalue = [0,8.27,9.06,9.91,9.82,10.63,11.05,11.78,11.27,11.3,12.15]
   numberofshares = [3076,3036,2956,2828,2712,2624,2523,2457,2414,2395,2345]
   pe_ratio = [58.1,25.9,16.7,19.7,42.2,29.3,30.4,30,31.4,40.7,34]
   pb_ratio = [58.1,25.9,16.7,19.7,42.2,29.3,30.4,30,31.4,40.7,34]
   
   datadictionary = {'year':year, 
                     'roe':roe,
                     'fcfps':fcfps,
                     'eps':eps,
                     'dividend':dividend,
                     'payout_ratio':payout_ratio,
                     'bookvalue':bookvalue,
                     'numberofshares':numberofshares,
                     'pe_ratio':pe_ratio,
                     'pb_ratio':pb_ratio}
   
   return datadictionary
 
def generate_csv_skeleton(directory='',filename=''):
   '''
   Function to generate skeleton code to copy raw data into
   '''
   if (directory==''):
      directory = 'sample_data/skeletons/'
   if (filename==''):
      filename = 'csv_skeleton_data.csv'
   file = open(directory+filename, 'w')
   
   # create the header row
   file.write('Year,')
   for i in range(10):
      file.write(str(i+2009))
      file.write(',')
   file.write('TTM\n')
   
   file.write('Earnings per share\n')
   file.write('Dividends\n')
   file.write('Payout Ratio\n')
   file.write('Shares\n')
   file.write('Book Value Per Share\n')
   file.write('Free Cash Flow Per Share\n')
   file.write('Return on Equity %\n')
   file.write('Price-Earnings Ratio\n')
   file.write('Price-Book Ratio\n')
   file.close()
   file=None
   return

if __name__ == '__main__':
   generate_csv_skeleton()