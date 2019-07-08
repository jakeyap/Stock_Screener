# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:58:14 2018

This file is just for plotting the data out nicely

Important things to plot are:

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
   
@author: Yong Keong
"""

import matplotlib.pyplot as plt


def plot_data(year_arr, data, title, folder):
    plt.plot(year_arr, data)
    plt.title(title)
    #plt.savefig('C:/Users/Yong Keong/Documents/GitHub/Stock_Screener/'+folder+title+'.png')
    plt.savefig(folder+title+'.png')
    
def plot_full_dataset(data, title='', folder=''):
   year = data['year']
   plt.figure(figsize=(12,9))
   plt.suptitle(title)
   plt.rcParams.update({'font.size': 7})
   
   eps = data['eps']
   roe = data['roe']
   payout_ratio = data['payout_ratio']
   dividend = data['dividend']
   bookvalue = data['bookvalue']
   numberofshares = data['numberofshares']
   fcfps = data['fcfps']
   pe_ratio = data['pe_ratio']
   pb_ratio = data['pb_ratio']
   
   plt.subplot(2,3,1)
   plt.title('Blue: EPS, red: div, green: FCFPS')
   plt.plot(year, eps, color='blue')
   plt.plot(year, dividend, color='red')
   plt.plot(year, fcfps, color='green')
   plt.grid(True)
   
   plt.subplot(2,3,4)
   plt.title('Blue: Payout ratio, red: ROE')
   plt.plot(year, payout_ratio, color='blue')
   plt.plot(year, roe, color='red')
   plt.grid(True)
   
   plt.subplot(2,3,3)
   plt.title('Shares')
   plt.plot(year, numberofshares)
   plt.grid(True)
   
   plt.subplot(2,3,2)
   plt.title('BVPS')
   plt.plot(year, bookvalue)
   plt.grid(True)
   
   plt.subplot(2,3,5)
   plt.title('PE ratio')
   plt.plot(year, pe_ratio)
   plt.grid(True)
   
   plt.subplot(2,3,6)
   plt.title('PB ratio')
   plt.plot(year, pb_ratio)
   plt.grid(True)
   
   plt.savefig(folder+title+'.png')