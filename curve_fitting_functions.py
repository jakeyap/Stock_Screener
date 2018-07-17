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

'''
UNTIL HERE YK 20180717
'''