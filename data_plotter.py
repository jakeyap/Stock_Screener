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
   
   plt.figure(title)
   plt.figure(figsize=(12,9))
   eps = data['eps']
   roe = data['roe']
   payout_ratio = data['payout_ratio']
   dividend = data['dividend']
   bookvalue = data['bookvalue']
   numberofshares = data['numberofshares']
   fcfps = data['fcfps']
   pe_ratio = data['pe_ratio']
   
   plt.subplot(3,3,1)
   plt.title('Blue: EPS, red: div')
   plt.plot(year, eps, color='blue')
   plt.plot(year, dividend, color='red')
   plt.grid(True)
   
   plt.subplot(3,3,2)
   plt.title('Payout ratio')
   plt.plot(year, payout_ratio)
   plt.grid(True)
   
   plt.subplot(3,3,3)
   plt.title('ROE')
   plt.plot(year, roe)
   plt.grid(True)
   
   plt.subplot(3,3,4)
   plt.title('BVPS')
   plt.plot(year, bookvalue)
   plt.grid(True)
   
   plt.subplot(3,3,5)
   plt.title('Shares')
   plt.plot(year, numberofshares)
   plt.grid(True)
   
   plt.subplot(3,3,6)
   plt.title('FCFPS')
   plt.plot(year, fcfps)
   plt.grid(True)
   
   plt.subplot(3,3,7)
   plt.title('PE')
   plt.plot(year, pe_ratio)
   plt.grid(True)
   
   plt.subplot(3,3,8)
   plt.title('')
   #plt.plot(year, )
   plt.grid(True)
   
   plt.subplot(3,3,9)
   plt.title('')
   #plt.plot(year, )
   plt.grid(True)
   
   plt.savefig(folder+title+'.png')