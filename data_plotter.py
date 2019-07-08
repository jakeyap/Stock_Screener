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
    
def plot_full_dataset(data, title='', directory='', projectionyear=0):
   '''
   Function to plot out the whole dictionary of stats
   Arguments:
      data: dictionary of company stats
      title: title of plots
      directory: folder to save the plots in
      projectionyear: where to start shading from. if 0, dont shade
   '''
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
   
   stockprice = []
   counter = 0
   while counter < len(year):
      stockprice.append(pe_ratio[counter] * eps[counter])
      counter = counter + 1
   
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
   plt.title('Blue:BVPS, red: stock')
   plt.plot(year, bookvalue,color='blue')
   plt.plot(year, stockprice,color='red')
   plt.grid(True)
   
   plt.subplot(2,3,5)
   plt.title('PE ratio')
   plt.plot(year, pe_ratio)
   plt.grid(True)
   
   plt.subplot(2,3,6)
   plt.title('PB ratio')
   plt.plot(year, pb_ratio)
   plt.grid(True)
   
   shade_projections(projectionyear);
   
   plt.savefig(directory+title+'.png')
   

def shade_projections(year):
   '''
   Function to shade the projection area
   '''
   if (year == 0):
      pass
   else:
      for index in range(1,7):
         plt.subplot(2,3,index)
         axes = plt.gca()
         ylimits = axes.get_ylim()
         xlimits = axes.get_xlim()
         axes.fill_betweenx(ylimits, year, xlimits[1], color='green',alpha=0.1)
         axes.set_ylim([ylimits[0], ylimits[1]])
         axes.set_xlim([xlimits[0], xlimits[1]])
   return