# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:57:31 2018
File under test:
    curve_fitting_functions.py
    

@author: Yong Keong
"""
import curve_fitting_functions as fitting
import matplotlib.pyplot as plt

earnings = [4.05e9, 4.45e9,4.24e9,4.37e9]
year0 = [1,2,3,4]
year1 = [2014,2015,2016,2017]

# Switch between real years & indexed from 0 years to test data
year = year1

''' Projection of 10 years into the future '''
# Create the 10 year projection array first
# Create a copy
proj_year = year.copy()
# Find the last year with valid data
last_year = year[len(year)-1]
counter = 1
while counter <= 10:
    proj_year.append(last_year + counter)
    counter = counter + 1

''' Do the actual regression to get the factors '''
[log1, log0] = fitting.fit_logarithm(year, earnings)
[lin1, lin0] = fitting.fit_linear(year, earnings)
[exp1, exp0] = fitting.fit_exponential(year, earnings)

''' Create 3 regression lines data '''
x_vals = year
y_vals_exp = fitting.project_exponential(proj_year, exp1, exp0)
y_vals_lin = fitting.project_linear(proj_year, lin1, lin0)
y_vals_log = fitting.project_log(proj_year, log1, log0)

plt.plot(year, earnings)
plt.plot(proj_year, y_vals_exp)
plt.plot(proj_year, y_vals_lin)
plt.plot(proj_year, y_vals_log)
plt.grid('on')

'''
Rescale the yaxis
'''
axes = plt.gca()
ans = axes.get_ylim()
axes.set_ylim([0,ans[1]])

"""
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

"""