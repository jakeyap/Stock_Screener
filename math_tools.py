# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 00:29:28 2019

@author: Yong Keong
"""
import numpy as np
import generate_test_data as generator
import matplotlib.pyplot as plt
import scipy.stats as stats

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
        period_mean = sum (datalist[index+1-num_periods : index+1]) / num_periods
        band_mid.append(period_mean)
        
        period_std = 0
        for each in datalist[index+1-num_periods : index+1]:
            period_std = period_std + (each - period_mean)**2
        period_std = np.sqrt(period_std) / num_periods
        band_top.append( period_mean + std_multiplier * period_std )
        band_bot.append( period_mean - std_multiplier * period_std )
        index = index + 1
       
    return {'bollinger_top': band_top,
            'bollinger_mid': band_mid,
            'bollinger_bot': band_bot}

def generate_bollinger_roe(data_dict, std_mult=3, num_periods=5):
    '''
    Takes the above bollinger band function and runs it on ROE.
    args: data_dict is a dictionary of stock data
    returns a dictionary, same as above function
    '''
    hist_roe = data_dict ['roe']   
    return generate_bollinger_bands(hist_roe, std_multiplier=std_mult, num_periods=num_periods)

def generate_single_norm_dist(mean=0,std=1, resolution=20, width_of_bell=3):
    '''
    Generates PDF of a normal distribution. 
    Truncates and approximates into buckets.
    Rescales so that the sum is 1
    Args:
        mean: mean of normal distribution
        std : standard dev of normal distribution
        resolution: how many steps are in this normal dist
        width_of_bell: how many SDs away from mean to check. default is 3
    Returns:
        list of 2 lists [xvals, yvals]
        xvals: list of xvalues on a normal distribution
        yvals: list of yvalues on a normal distribution
    '''
    xvals = np.array(range(-resolution, resolution+1))
    xvals = xvals * width_of_bell / resolution
    random_variable = stats.norm()
    yvals = random_variable.pdf(xvals)
    # do the rescaling here so that the bars sum to 1
    yvals = yvals * (width_of_bell / resolution)
    
    # rescale x axis to get the right mean and spread values
    xvals = xvals * std + mean
    return [xvals, yvals]
   
def generate_2axis_norm_dist(xmean, xstd, ymean, ystd, resolution=20, width_of_bell=3):
    '''
    Same as above except for 2 dimension input
    Args:
        mean: mean of normal distribution
        std : standard dev of normal distribution
        resolution: how many steps are in this normal dist
        width_of_bell: how many SDs away from mean to check. default is 3
    Returns:
        list of 2 lists [xvals, yvals]
        xvals: list of xvalues on 1st axis of normal distribution
        yvals: list of yvalues on 2nd axis of normal distribution
        zvals: list of zvalues outputs of normal dist
    '''
    xvals, zvals1 = generate_single_norm_dist(mean=xmean, std=xstd, resolution=resolution, width_of_bell=width_of_bell)
    yvals, zvals2 = generate_single_norm_dist(mean=ymean, std=ystd, resolution=resolution, width_of_bell=width_of_bell)
    
    xlength = xvals.shape[0]
    ylength = yvals.shape[0]
    
    zvals1 = zvals1.reshape(xlength,1)
    zvals2 = zvals2.reshape(1,ylength)
    
    zvals = np.dot(zvals1,zvals2)
    return [xvals, yvals, zvals]
   
def generate_discount_rate(risk_free_rate=0.01, num_years=10, success_rate = 0.33):
    # generates a discount rate based on risk free rate, failure likelihood
    # prob_success x [1 + r]^n >= [1 + rfr]^n
    # [1 + r] >= [1 + rfr] / [prob_success ^ (1/n)]
    # r >= [1 + rfr] / [prob_success ^ (1/n)] - 1
    
    numer = 1 + risk_free_rate
    denom = success_rate ** (1/num_years)
    
    return (numer/denom) - 1
    

if __name__ == '__main__':
#   fakedata = generator.generate()
#   year = fakedata['year']
#   roes = fakedata['roe']
#   boil_bands = generate_bollinger_roe(fakedata, std_mult=3, num_periods=2)
#   boil_top = boil_bands['bollinger_top']
#   boil_mid = boil_bands['bollinger_mid']
#   boil_bot = boil_bands['bollinger_bot']
#   plt.plot(year,roes,color='red')
#   plt.plot(year,boil_top,color='blue')
#   plt.plot(year,boil_mid,color='blue')
#   plt.plot(year,boil_bot,color='blue')
   
#   xvals, yvals = generate_single_norm_dist(mean=10,std=10,resolution=20) 
#   plt.bar(xvals,yvals)
#   sum(yvals)

    xvals, yvals, zvals = generate_2axis_norm_dist(10,0.1,0,1,20) 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Grab some test data.
    X, Y = np.meshgrid(xvals, yvals)
    # Plot a basic wireframe.
    #ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    ax.plot_wireframe(X, Y, zvals, color='red')