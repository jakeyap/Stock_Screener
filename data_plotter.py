# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:58:14 2018

This file is just for plotting the data out nicely. 
It takes in a summarized data dictionary.

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
import matplotlib.ticker as ticker
import numpy as np
from mpl_toolkits.mplot3d import axes3d

def plot_data(year_arr, data, title, folder):
    plt.plot(year_arr, data)
    plt.title(title)
    #plt.savefig('C:/Users/Yong Keong/Documents/GitHub/Stock_Screener/'+folder+title+'.png')
    plt.savefig(folder+title+'.png')
    
def plot_full_dataset(data, title='', directory='', 
                      projectionyear=0, annotate_string=None,
                      bollingerdata = None):
    '''
    Function to plot out the whole dictionary of stats
    Arguments:
       data: dictionary of company stats
       title: title of plots
       directory: folder to save the plots in
       projectionyear: where to start shading from. if 0, dont shade
       annotate_data: for plugging in the dictionary of roe, pe
       bollingerdata: for plotting bollinger bands. If None, do nothing
    '''
    # define place to store plots
    plot_directory = directory + 'generated_plots/'
    
    year = data['year']
    plt.figure(figsize=(12,9))
    plt.suptitle(title,size=12)
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
    try:
        leverage_ratio = data['leverage_ratio']
    except Exception:
        leverage_ratio = [0] * len(pb_ratio)

    stockprice = []   
    counter = 0
    while counter < len(year):
        stockprice.append(pe_ratio[counter] * eps[counter])
        counter = counter + 1
   
    plot1 = plt.subplot(2,3,1)
    plt.title('Blue: EPS, red: div, green: FCFPS')
    plt.plot(year, eps, color='blue')
    plt.plot(year, dividend, color='red')
    plt.plot(year, fcfps, color='green')
   
    plot2 = plt.subplot(2,3,4)
    plt.title('Blue: Payout ratio, red: ROE')
    plt.plot(year, payout_ratio, color='blue')
    plt.plot(year, roe, color='red')
    if bollingerdata is not None:
        bollinger_roe_top = bollingerdata['bollinger_top']
        bollinger_roe_mid = bollingerdata['bollinger_mid']
        bollinger_roe_bot = bollingerdata['bollinger_bot']
        print(year)
        print(bollinger_roe_top)
        plt.plot(year,bollinger_roe_top,'--',color='red')
        plt.plot(year,bollinger_roe_mid,'--',color='red')
        plt.plot(year,bollinger_roe_bot,'--',color='red')
   
    plot3 = plt.subplot(2,3,3)
    plt.title('Shares')
    plt.plot(year, numberofshares)
    
    plot4 = plt.subplot(2,3,2)
    plt.title('Blue:BVPS, red: stock')
    plt.plot(year, bookvalue,color='blue')
    plt.plot(year, stockprice,color='red')
    
    plot5 = plt.subplot(2,3,5)
    plt.title('Blue: PB, red: PE, green: leverage')
    plt.plot(year, pe_ratio, color='red')
    plt.plot(year, pb_ratio, color='blue')
    plt.plot(year, leverage_ratio, color='green')
    
    plt.subplot(2,3,6)
    plt.ylim([0,1])
    plt.xlim([0,1])
    annotate_graph(annotate_string)
    
    plotlist = [plot1, plot2, plot3, plot4, plot5]
    for eachplot in plotlist:
        axes = eachplot.axes
        axes.grid(True)
        yearbase = round(len(year) / 10)
        axes.xaxis.set_major_locator(ticker.IndexLocator(base=yearbase, offset=0))
    
    shade_projections(plotlist, projectionyear);
    plt.tight_layout(pad=4)
    plt.savefig(plot_directory+title+'.png')
      
def annotate_graph(annotate_string):
    if (annotate_string is None):
        return
    else:
        axes = plt.gca()
        ylimits = axes.get_ylim()
        xlimits = axes.get_xlim()
        xplace = 0.5 * (xlimits[1] - xlimits[0]) + xlimits[0]
        yplace = 0.5 * (ylimits[1] - ylimits[0]) + ylimits[0]
        plt.annotate(annotate_string, xy=(xplace,yplace),size=13,ha='center',va='center')
        return

def shade_projections(plotlist, year):
    '''
    Function to shade the projection area
    '''
    if (year == 0):
        pass
    else:
        for each in plotlist:
            axes = each.axes
            ylimits = axes.get_ylim()
            xlimits = axes.get_xlim()
            axes.fill_betweenx(ylimits, year, xlimits[1], color='green',alpha=0.1)
            axes.set_ylim([ylimits[0], ylimits[1]])
            axes.set_xlim([xlimits[0], xlimits[1]])
    return

def plot_countour(pe_points,roe_points,presentvalues, 
                  directory='',
                  title='',
                  stringtoprint=''):
    plot_directory = directory + 'generated_plots/'
    plt.figure(figsize=(12,9))
    ax = plt.gca()
    X, Y = np.meshgrid(pe_points, roe_points)
    CS = plt.contour(X, Y, presentvalues)
    ax.clabel(CS, inline=1, fontsize=10)
    plt.grid(True)
    plt.suptitle(title+'\n'+stringtoprint,size=10)
    plt.ylabel('Different ROEs')
    plt.xlabel('Different PE ratios')
    plt.savefig(plot_directory+title+'_contour.png')

def plot_wireframe(pe_points,roe_points,presentvalues, currentprice=None,color='red',
                   title='',
                   directory='',
                   stringtoprint=''):
    plot_directory = directory + 'generated_plots/'
    fig = plt.figure(figsize=(12,9))
    ax = fig.add_subplot(111, projection='3d')
    # Grab some test data.
    X, Y = np.meshgrid(pe_points, roe_points)
    # Plot a basic wireframe.
    ax.plot_wireframe(X, Y, presentvalues, color=color)
    if currentprice is not None:
        ref = np.ones(shape=presentvalues.shape) * currentprice
        ax.plot_wireframe(X, Y, ref, color='gray')
    plt.suptitle(title+'\n'+stringtoprint,size=10)
    plt.ylabel('Different ROEs')
    plt.xlabel('Different PE ratios')
    plt.show()
    plt.savefig(plot_directory+title+'_parameterized_2.png')