# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:24:01 2019

This is supposed to take raw data and make estimates of figures of merit
Return min, max, mean, std dev of the 
   EPS,
   ROE
   Payout ratio
   PE
   PB
   
Estimating future data requires estimates of 
   ROE, payout ratio, PE, PB
   returns a list of dividends across years
   discount rate
   
@author: Yong Keong
"""

import numpy as np

def analyze_metric(data, name=''):
    '''
    Generic function to extract min max avg std from a list
    Arguments: 
        data: a list of numbers
        name: a name for dictionary entries
    Returns:
        a dictionary with names
        {name_min: smallest number in list
        name_max: largest number in list
        name_avg: mean of list
        name_std: st dev of list
        }
    '''
    data_min = np.min(data)
    data_max = np.max(data)
    data_avg = np.average(data)
    data_std = np.std(data)
    
    return {(name+'_min'): data_min,
            (name+'_max'): data_max,
            (name+'_avg'): data_avg,
            (name+'_std'): data_std}

def analyze_pe_ratio(data):
    '''
    Function to get the 4 stats of PE ratio
    Arguments: data, a dictionary of datapoints
    Returns: a dictionary of 
    {   pe_min: smallest number in pe list
        pe_max: largest number in pe list
        pe_avg: mean of pe list
        pe_std: st dev of pe list
    }
    '''
    pe_ratio_data = data['pe_ratio']
    pe_stats = analyze_metric(pe_ratio_data, 'pe_ratio')
    return pe_stats
   
def analyze_pb_ratio(data):
    '''
    Same as above, except for PB
    '''
    pb_ratio_data = data['pb_ratio']
    pb_stats = analyze_metric(pb_ratio_data, 'pb_ratio')
    return pb_stats

def analyze_roe(data):
    '''
    Same as above, except for ROE
    '''
    roe_data = data['roe']
    roe_stats = analyze_metric(roe_data, 'roe')
    return roe_stats

def analyze_payout_ratio(data):
    '''
    Same as above, except for payout_ratio
    '''
    payout_ratio_data = data['payout_ratio']
    payout_ratio_stats = analyze_metric(payout_ratio_data, 'payout_ratio')
    return payout_ratio_stats

def analyze_eps(data):
    '''
    Same as above, except for earnings per share
    '''
    eps_data = data['eps']
    eps_stats = analyze_metric(eps_data, 'eps')
    return eps_stats

def analyze_all_data(data, showstats=False):
    '''
    Same as above, and does everything in one step
    Input: 
       data: a dictionary of stock data
       show_stats: decide whether to print on console the summarize stats
    Returns: a dictionary with 
       (min max avg std) of (pe pb roe eps payout_ratio)
    '''
    pe_stats = analyze_pe_ratio(data)
    pb_stats = analyze_pb_ratio(data)
    roe_stats = analyze_roe(data)
    payout_ratio_stats = analyze_payout_ratio(data)
    eps_stats = analyze_eps(data)
    
    stats_dictionary = {}
    stats_dictionary.update(pe_stats)
    stats_dictionary.update(pb_stats)
    stats_dictionary.update(roe_stats)
    stats_dictionary.update(payout_ratio_stats)
    stats_dictionary.update(eps_stats)
    
    if (showstats):
        print_stats(stats_dictionary)
       
    return stats_dictionary


def print_stats(stats):
    footers = ['_min','_max','_avg','_std',]
    headers = ['pe_ratio','pb_ratio','roe','payout_ratio','eps']
    
    stat_names = []
    for each_header in headers:
        for each_footer in footers:
            stat_names.append(each_header+each_footer)
    
    counter = 0
    for each_name in stat_names:
        number = round(stats[each_name],2)
        print(each_name+':\t\t'+ str(number))
        if (counter == 3):
            print('===============')
            counter=0
        else:
            counter = counter + 1