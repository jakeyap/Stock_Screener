# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 00:29:28 2019

@author: Yong Keong
"""
import numpy as np

def generate_bollinger_bands(datalist, std_multiplier, num_periods):
   '''
   Takes a list of data. Spits out the bollinger bands as lists.
   Args: 
      datalist: list of time series data points
      std_multiplier: a number to multiply the std by to obtain the width
      num_periods: a number to calculate the moving averages over
   Returns: a dictionary
   {'bollinger_top': list of data points for top bollinger band
    'bollinger_mid': list of data points for mid bollinger band
    'bollinger_bot': list of data points for bot bollinger band
   }
   '''
   band_top = []
   band_mid = []
   band_bot = []
   
   datalen = len(datalist)
   index = 0
   # Padding with Nones
   while index < num_periods-1:
      band_top.append(None)
      band_mid.append(None)
      band_bot.append(None)
      index = index + 1
      
   while index < datalen:
      period_mean = sum (datalist[index-num_periods:index+1]) / num_periods
      band_mid.append(period_mean)
      
      period_std = 0
      for each in datalist[index-num_periods:index]:
         period_std = period_std + (each - period_mean)**2
      period_std = np.sqrt(period_std) / num_periods
      band_top.append( period_mean + std_multiplier * period_std )
      band_bot.append( period_mean - std_multiplier * period_std )
      index = index + 1
      
   return {'bollinger_top': band_top,
           'bollinger_mid': band_mid,
           'bollinger_bot': band_bot}

def generate_bollinger_roe(data_dict, std_mult=3, num_periods=5):
   hist_roe = data_dict ['roe']   
   return generate_bollinger_bands(hist_roe, std_multiplier=std_mult, num_periods=num_periods)