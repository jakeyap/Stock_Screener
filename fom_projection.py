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
    'leverage_ratio':leverage_ratio
   
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
    new_data['year'].append(int(last_year))
    
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
    try:
        # pad the leverage ratio with leverage ratio
        leverage_ratio = data['leverage_ratio'][-1]
        new_data['leverage_ratio'].append(leverage_ratio)
    except Exception:
        pass
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

def estimate_final_stock_price(data):
    '''
    A function to get the final stock price when selling
    Arguments:
        data: dictionary to store everything
    Returns:
        stockprice: float for stock price at the end based on PE
    '''
    pe_ratio = data['pe_ratio']
    eps = data['eps']
    return pe_ratio[-1] * eps[-1]

def get_cashflow_list(year, data, taxrate=0):
    '''
    Function to get the cashflows starting from this year 
    Arguments:
        year: an integer of when you want to put in money to buy
        data: dictionary
    Returns a list of cashflows starting from input year
    '''
    year_list = data['year']
    # find the index of the year
    index = year_list.index(year)
    temp_list = data['dividend']
    dividend_list = temp_list.copy()
    dividend_list = dividend_list[index:]
    for i in range(len(dividend_list)):
        dividend_list[i] = dividend_list[i] * (1-taxrate/100)
    return dividend_list

def dcf_calculator(year, data, discount_rate=5, taxrate=0):
    '''
    Calculates the present value of a stock 
    Assumes some dividends and selling price at the end
    
    Arguments: 
        year: integer of the current year
        data: dictionary of real and predicted values
        discount rate: % discount rate for DCF
    Returns: 
        a number, present value
    '''
    dividends = get_cashflow_list(year,data,taxrate)
    finalstockprice = estimate_final_stock_price(data)
    # print('Terminal stock price shld be '+str(round(finalstockprice,2)))
    # Need to include the selling price at the end
    dividends[-1] = dividends[-1] + finalstockprice
    return dcf_core(cashflowlist = dividends, discount_rate = discount_rate)

def dcf_core(cashflowlist, discount_rate=5):
    '''
    A function to backcalculate the present value of a cashflow
    Arguments: 
        cashflowlist: list of cashflows
    '''
    discount_factor = 1 + (discount_rate / 100)
    length = len(cashflowlist)
    pv = 0
    counter = 0
    while (counter < length):
        denom = discount_factor**(counter+1)
        numer = cashflowlist[counter]
        pv = pv + (numer / denom)
        counter = counter + 1
    return round(pv,3)
