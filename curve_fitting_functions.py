# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:47:44 2018
This file contains all the functions to fit curves.
It has 3 scenarios to model earnings.

Optimistic:  exponential growth
Realistic:   linear growth
Pessimistic: log growth 

Figure out the fitted curves and draw over existing data
Plot another 10 year and predict future earnings

================================================
LINEAR MODEL
earnings = gradient x year + intercept
================================================
EXPONENTIAL GROWTH MODEL
earnings = A x (B ** year)
log(earnings) = log A + year x log (B)
================================================
LOG GROWTH MODEL
earnings = logscale x log (year) + logoffset
================================================

@author: Yong Keong
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_earnings(year_arr, earnings_arr, proj_data, title):
    '''
    To create an array with the projections
    
    Inputs:
        year_arr: array of years
        earnings_arr: array of earnings
        proj_data: where
            proj_year  = proj_data[0]
            y_vals_exp = proj_data[1]
            y_vals_lin = proj_data[2]
            y_vals_log = proj_data[3]
            exp_label = proj_data[4]
            lin_label = proj_data[5]
            log_label = proj_data[6]
        title: a string to put on the plot
    Outputs:
        None
        A plot with title: title, but is not returned
    '''
    plt.figure(title)
    proj_year  = proj_data[0]
    y_vals_exp = proj_data[1]
    y_vals_lin = proj_data[2]
    y_vals_log = proj_data[3]
    exp_label = proj_data[4]
    lin_label = proj_data[5]
    log_label = proj_data[6]

    plt.plot(year_arr, earnings_arr, marker='x')
    plt.plot(proj_year, y_vals_exp, linestyle='--', color='green', label=exp_label)
    plt.plot(proj_year, y_vals_lin, linestyle='-.', color='grey', label=lin_label)
    plt.plot(proj_year, y_vals_log, linestyle='--', color='red', label=log_label)
    plt.grid('on')
    plt.title(title)
    plt.legend()
    
    axes = plt.gca()
    ylimits = axes.get_ylim()
    axes.set_ylim([0, ylimits[1]])
    xlimits = [proj_year[0], proj_year[len(proj_year)-1]]
    axes.set_xlim(xlimits)
    xlimits = axes.get_xlim()
    last_year = year_arr[len(year_arr)-1]
    axes.fill_betweenx([0, ylimits[1]], last_year, xlimits[1], color='green',alpha=0.1)
    return


def create_projections(year_arr, earnings_arr, projection_len=10):
    '''
    For creating the projections
    Input:
        year_arr: actual years
        earnings_arr: actual earnings data
        projection_len=10: number of years to predict
    Outputs:
        [
        proj_year_arr: real and projected years
        y_vals_exp: exponential fit
        y_vals_lin: linear fit
        y_vals_log: log fit
        exp_label: label to put on the graph
        lin_label: label to put on the graph
        log_label: label to put on the graph
        ]
    '''
    # Regression line coefficients
    [log1, log0] = fit_logarithm(year_arr, earnings_arr)
    [lin1, lin0] = fit_linear(year_arr, earnings_arr)
    [exp1, exp0] = fit_exponential(year_arr, earnings_arr)
    
    # Create the 10 year projection array first
    proj_year = year_arr.copy()
    # Find the last year with valid data
    last_year = year_arr[len(year_arr)-1]
    counter = 1
    while counter <= projection_len:
        proj_year.append(last_year + counter)
        counter = counter + 1
    
    # Create the projected data
    y_vals_exp = project_exponential(proj_year, exp1, exp0)
    y_vals_lin = project_linear(proj_year, lin1, lin0)
    y_vals_log = project_log(proj_year, log1, log0)
    exp_label = str('Exponetial: y = %.2e * ( 1 + (%1.3f))**N' %(exp1,exp0-1))
    lin_label = str('Linear fit: y = %.3e * x + (%.2e)' % (lin1,lin0))
    log_label = str('Log fit:    y = %.3e * log(x) + %.3e' % (log1, log0))
    
    return [proj_year,y_vals_exp, y_vals_lin, y_vals_log, exp_label, lin_label, log_label]


def fit_exponential(year, earnings):
    """
    Inputs: 
        year (an array)
        earnings (an array)
    Outputs:
        A (a scalar base number)
        B = 1+ROR for compounding
    ================================================
    EXPONENTIAL GROWTH MODEL 
        where ROR = rate of return
    earnings = A x (B ** year)
    log(earnings) = log A + year x log (B)
    
    Regression will return 
    ans1 = log B
    ans0 = log A
    
    To get back to compounding equation,
    A = 10**ans0
    B = 10**ans1
    """
    [ans1, ans0] = np.polyfit((year), np.log10(earnings), 1)
    A = 10**ans0
    B = 10**ans1
    return [A,B]

def fit_linear(year, earnings):
    """
    Inputs: 
        year (an array)
        earnings (an array)
    Outputs:
        gradient (a scalar number)
        intecept (a scalar number)
    """
    [gradient, intercept] = np.polyfit((year), earnings, 1)    
    return [gradient, intercept]

def fit_logarithm(year, earnings):
    """
    LOG GROWTH MODEL
    earnings = logscale x log (year) + logoffset
    
    Regression will return
    ans1 = logscale
    ans0 = logoffset
    
    There is a quirk with log fitting. 
    You have to remove the year offset
    Do this by scaling year so that years always start from Y1
    """
    year_rescaled = np.subtract(year,year[0]-1)
    [logscale, logoffset] = np.polyfit(np.log10(year_rescaled), earnings,1)
    return [logscale, logoffset]

def project_linear(proj_year, gradient, intercept):
    '''
    Inputs: 
        proj_year: years for prediction
        gradient, intercept: scalar factors, self explanatory
    Outputs:
        proj_lin: array of predicted values using linear growth
    '''
    temp = np.multiply(gradient, proj_year)
    proj_lin = np.add(temp, intercept)
    
    return proj_lin

def project_log(proj_year, logscale, logoffset):
    '''
    Inputs: 
        proj_year: years for prediction
        logscale, logoffset: scalar factors, where
        earnings = logscale x log (year) + logoffset
    Outputs:
        proj_log: array of predicted values using linear growth
        
        IMPORTANT: Remember to take care of year offset
    '''
    year_rescaled = np.subtract(proj_year,proj_year[0]-1)
    temp0 = np.log10(year_rescaled)
    temp1 = np.multiply(temp0, logscale)
    proj_log = np.add(temp1,logoffset)
    return proj_log

def project_exponential(proj_year, A, B):
    '''
    Inputs: 
        proj_year: years for prediction
        A, B: scalar factors, where
        earnings = A x (B ** year)
    Outputs:
        proj_exp: array of predicted values using exponential growth
    '''
    temp0 = np.power(B, proj_year)
    proj_exp = np.multiply(temp0, A)
    return proj_exp

def earnings_consistency_check(year, earnings_arr, regression_arr):
    end_index = len(year)
    counter = 0
    consistent = True
    while counter < end_index:
        if ( earnings_arr[counter] < regression_arr[counter] * 0.5):
            consistent = False
            print('Earnings in year %d is poor' % year[counter])
        else:
            print('Earnings in year %d is OK' % year[counter])
        counter = counter + 1
    return consistent
    
    
'''
UNTIL HERE YK 20180717
'''