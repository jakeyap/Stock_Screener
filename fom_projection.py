# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:29:53 2019
Takes estimates of
   ROE, payout ratio, PE, PB
   to generate predicted returns in the future
   discount rate
   
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

import copy

def modify_dataset_one_year_simple(data, predicted_stats):
   '''
   Takes a fixed ROE, fixed payout ratio and predict future
   Arguments: 
      data: a dictionary of all the years of data
      predicted_stats: dict of (pe pb payout eps roe)
   Returns:
      new_data, modified to predict company situation 1 year later
   '''
   expected_roe = predicted_stats['roe_avg']
   expected_payout_ratio = predicted_stats['payout_ratio_avg']
   expected_pe = predicted_stats['pe_ratio_avg']
   expected_pb = predicted_stats['pb_ratio_avg']
   
   new_data = copy.deepcopy(data)
   # append year
   last_year = new_data['year'][-1] + 1 # access last element and add 1
   new_data['year'].append(last_year)
   
   # pad ROE
   new_data['roe'].append(expected_roe)
   
   # pad the fcfps with copy of last element
   fcfps = new_data['fcfps'][-1]
   new_data['fcfps'].append(fcfps)
   
   # calculate & append EPS from ROE & last book value
   lastbookvalue = data['bookvalue'][-1]
   new_eps = lastbookvalue * expected_roe / 100
   new_data['eps'].append(new_eps)
   
   # calculate & append dividend from payout ratio & EPS
   new_dividend = new_eps * expected_payout_ratio / 100
   new_data['dividend'].append(new_dividend)
   
   # pad the payout ratio
   new_data['payout_ratio'].append(expected_payout_ratio)
   
   # calculate retained earnings by subtracting div from eps
   retained_earning = new_eps - new_dividend
   
   # calculate & append new book value by adding past BV and retained eps
   newbookvalue = lastbookvalue + retained_earning
   new_data['bookvalue'].append(newbookvalue)
   
   # pad numberofshares
   numberofshares = data['numberofshares'][-1]
   new_data['numberofshares'].append(numberofshares)
   
   # pad the pe ratio with expected value
   new_data['pe_ratio'].append(expected_pe)
   
   # pad the pb ratio with expected value
   new_data['pb_ratio'].append(expected_pb)
   
   return new_data

def modify_dataset_multi_year(data, predicted_stats, years=10):
   '''
   Does the same as the modify_dataset_one_year(), iterated over years
   Arguments: 
      data: a dictionary of all the years of data
      predicted_stats: dict of (min max avg std) x (pe pb payout eps roe)
      years: integer to loop over
   Returns:
      data: modified to predict company situation N years later
   '''
   data_copy = None
   data_old = data
   for index in range(years):
      data_copy = modify_dataset_one_year_simple(data_old, predicted_stats)
      data_old = data_copy
   return data_copy