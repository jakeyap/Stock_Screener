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
    ================================================
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
    ================================================
    LOG GROWTH MODEL
    earnings = logscale x log (year) + logoffset
    
    Regression will return
    ans1 = logscale
    ans0 = logoffset
    
    There is a quirk with log fitting. 
    You have to remove the year offset
    Do this by scaling year so that years always start from Y1
    ================================================
    """
    year_rescaled = np.subtract(year,year[0]-1)
    [logscale, logoffset] = np.polyfit(year_rescaled, earnings,1)
    return [logscale, logoffset]

'''
UNTIL HERE YK 20180716
'''


''' Create 3 regression lines data '''
x_vals = year
y_vals_lin = np.multiply(gradient,x_vals) + intercept
y_vals_exp = A * np.power((compound_rate),year)
y_vals_log = logscale * np.log10(year) + logoffset

''' Projection of 10 years into the future '''
# Create the 10 year projection array first
proj_year = []
counter = 0
while counter <= 10:
    index = len(year) - 1
    proj_year.append(year[index]+counter)
    counter = counter + 1
# Exponential growth
y_vals_exp_pro = A * np.power((compound_rate),proj_year)
# Linear growth
y_vals_lin_pro = np.multiply(gradient,proj_year) + intercept
# Log growth
y_vals_log_pro = np.multiply(logscale, np.log10(np.subtract(proj_year,year[0]-1)))
y_vals_log_pro = np.add(y_vals_log_pro, logoffset)


''' Set up the plotting of graph '''
plt.figure()
plt.plot(year,earnings)

axes = plt.gca()
axes.set_xticks(year)

# Generate the labels and legends
exp_label = str('Exponential fit: y = %.2e * ( 1 + (%1.3f))**N' %(A,compound_rate-1))
lin_label = str('Linear fit:      y = %.3e * x + (%.2e)' % (gradient,intercept))
log_label = str('Logarithmic fit: y = %.3e * log(x) + %.3e' % (logscale, logoffset))

exp_pro_label = str('Exponential projection')
lin_pro_label = str('Linear projection')
log_pro_label = str('Log projection')

# Plot real data
plt.plot(x_vals, earnings,marker='o',color='red', label = 'Earnings')
# Plot regressions over old data
plt.plot(x_vals, y_vals_exp,color='blue', label=exp_label)
plt.plot(x_vals, y_vals_lin,color='green', label=lin_label)
plt.plot(x_vals, y_vals_log,color='black', label=log_label)

# Plot projections cases
plt.plot(proj_year, y_vals_exp_pro, linestyle='--',marker='+',color='grey', label=exp_pro_label)
plt.plot(proj_year, y_vals_lin_pro, linestyle='--',marker='x',color='grey', label=lin_pro_label)
plt.plot(proj_year, y_vals_log_pro, linestyle='--',marker='+',color='grey', label=log_pro_label)

axes.set_xticks(year+proj_year)
xlabels = axes.get_xticklabels()
axes.set_xticklabels(year+proj_year, rotation = 45)

print(exp_label)
print(lin_label)
print(log_label)

plt.legend()
plt.grid('on')

