# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:58:14 2018

This file is just for plotting the data out nicely

@author: Yong Keong
"""

import matplotlib.pyplot as plt

def plot_data(year_arr, data, title, folder):
    plt.plot(year_arr, data)
    plt.title(title)
    #plt.savefig('C:/Users/Yong Keong/Documents/GitHub/Stock_Screener/'+folder+title+'.png')
    plt.savefig(folder+title+'.png')