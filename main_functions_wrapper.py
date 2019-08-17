# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:36:21 2019

@author: Yong Keong
"""

import generate_test_data
import data_plotter as plotter
import fom_estimation as analyser
import fom_projection as predictor
import extract_stock_data as extractor
import numpy as np
import math_tools as math

def analyze_data(directory='', filename='', title='test company',plot=True,showstats=True):
   '''
   A wrapper function to generate summarized stock stats and show it graphically
   Arguments:
      directory: the raw file directory
      filename: uh huh
      title: string to be saved into the plot
      plot: whether to plot the graphs or not
      showstats: whether to show the summary stats of data or not
   Returns: [stats, data]
      stats: a dictionary containing _min _max _avg _std of roe pe_ratio payout_ratio pb_ratio 
      data: a dictionary of the whole stock data
   '''
   if (filename==''): # no filename given, use generated fake data
      data = generate_test_data.generate()
   else:
      data = extractor.read_csv2data(directory, filename)
   
   bollinger_data = math.generate_bollinger_roe(data_dict=data,std_mult=3,num_periods=5)
   
   # Show the min, max, avg, std of the PE, PB, ROE, payout_ratio
   if showstats:
      print('Showing stats')
   stock_stats = analyser.analyze_all_data(data,showstats=showstats)
   hist_roe = stock_stats['roe_avg']
   hist_pe = stock_stats['pe_ratio_avg']
   stringtoprint = 'Historical ROE mean: '+str(round(hist_roe,2)) + '\n'
   stringtoprint = stringtoprint + 'Historical PE mean: '+str(round(hist_pe,2))
   # Plot the old data, save it
   if plot:
      plotter.plot_full_dataset(title=title+' data', directory=directory, data=data,
                                annotate_string=stringtoprint,
                                bollingerdata=bollinger_data)
   return [data, stock_stats]
   
def modify_stock_stats(stock_stats, est_roe=None, est_pe=None, est_payout_ratio=None):
   '''
   A function to manually change the ROE, PE, payout ratios to generate predictions
   Arguments: 
      stock_stats: a dictionary containing 
            _min 
            _max 
            _avg 
            _std of roe pe_ratio payout_ratio pb_ratio 
   Retuns the same dictionary reference
   '''
   if (est_roe is not None):
      stock_stats['roe_avg'] = est_roe
   if (est_pe is not None):
      stock_stats['pe_ratio_avg'] = est_pe
   if (est_payout_ratio is not None):
      stock_stats['payout_ratio_avg'] = est_payout_ratio
   return stock_stats

def project_data_by_roe(data, stock_stats, projectionyear=2019, years2project=5, title='test company',
                 discount_rate=5,taxrate=0,directory='',plot=True):
   '''
   A wrapper function to do prediction of a stock N number of years later
   '''
   new_data = predictor.modify_dataset_multi_year(data=data, predicted_stats=stock_stats, years=years2project)
   presentvalue = predictor.dcf_calculator(year=projectionyear,
                                  data=new_data,
                                  discount_rate=discount_rate,
                                  taxrate=taxrate)
   
   if (plot):
      est_roe = stock_stats['roe_avg']
      est_pe = stock_stats['pe_ratio_avg']
      stringtoprint = 'Long term ROE: ' + str(est_roe) +'\n'
      stringtoprint = stringtoprint + 'Estimated PE:  ' + str(est_pe) + '\n'
      stringtoprint = stringtoprint + 'Discount rate: ' + str(round(discount_rate,2)) + '%\n'
      stringtoprint = stringtoprint + 'Present value: '+str(presentvalue)
      
      plotter.plot_full_dataset(title=title+' predictions',
                                data=new_data, 
                                directory=directory, 
                                projectionyear=projectionyear,
                                annotate_string=stringtoprint)
      print(stringtoprint)
   return presentvalue

def sweep_parameters_roe_and_pe(discount_rate=5, payout_ratio=0, 
                                currentprice=None, 
                                resolution=20, 
                                projectionyear=2019,
                                taxrate=0,
                                directory='', filename='', 
                                title='test company',
                                bollinger_compensation=False,
                                std_multiplier=3,
                                years2project=5):
   '''
   sweeps ROE and PE across a range of +- 1sd across all time
   plug in ranges into the projection function
   Discount rate and payout ratios are parameters
   
   bollinger_compensation is a boolean. 
   If false, use ROE across all time to make estimates
   If true, use bollinger bands to estimate future ROEs
   '''
   # read ROE and PE stats first
   [data, stock_stats] = analyze_data(directory=directory, filename=filename, title=title, plot=False, showstats=False)
   pe_ratio_avg = stock_stats['pe_ratio_avg']
   pe_ratio_std = stock_stats['pe_ratio_std']
   roe_avg = stock_stats['roe_avg']
   roe_std = stock_stats['roe_std']
   
   if bollinger_compensation:
      bollinger_data = math.generate_bollinger_roe(data_dict=data,std_mult=1,num_periods=5)
      bollinger_top = bollinger_data['bollinger_top']
      bollinger_mid = bollinger_data['bollinger_mid']
      roe_avg = bollinger_mid[-1]
      roe_std = bollinger_top[-1] - roe_avg
      
   pe_stepsize = pe_ratio_std * std_multiplier / resolution
   roe_stepsize = roe_std * std_multiplier / resolution
   
   # generate the ROE and PE ranges
   steps = np.array(range(-resolution, resolution+1))
   steps = steps.reshape(1,2*resolution+1)
   #pe_steps = np.zeros(shape=(1,2*resolution))
   pe_steps = steps * pe_stepsize + pe_ratio_avg
   #roe_steps = np.zeros(shape=(1,2*resolution))
   roe_steps = steps * roe_stepsize + roe_avg
   
   # Generate up the table of possible present values
   presentvalues = np.zeros(shape=(pe_steps.shape[1], roe_steps.shape[1]))
   # Generate probability of weights
   _, _, prob_weights = math.generate_2axis_norm_dist(xmean=pe_ratio_avg,
                                                xstd=pe_ratio_std,
                                                ymean=roe_avg,
                                                ystd=roe_std,
                                                resolution=resolution,
                                                width_of_bell=std_multiplier)
   
   # Calculate all outcomes within the realm of 3SDs
   for i in range(pe_steps.shape[1]):
      for j in range(roe_steps.shape[1]):
         test_pe = pe_steps[0][i]
         test_roe = roe_steps[0][j]
         new_stock_stats = modify_stock_stats(stock_stats, est_roe=test_roe, est_pe=test_pe, est_payout_ratio=payout_ratio)
         presentvalue = project_data_by_roe(data=data, stock_stats=new_stock_stats, 
                                     projectionyear=projectionyear, 
                                     years2project=years2project, title='test company',
                                     discount_rate=discount_rate,
                                     taxrate=taxrate,
                                     directory='', plot=False)
         if presentvalue < 0:
            presentvalue = 0
         presentvalues[i][j] = presentvalue
   
   # Calculate EV for each outcome and come up with a full EV
   expected_value = presentvalues * prob_weights
   expected_value = np.sum(expected_value)
   
   stringtoprint = 'discount rate: ' + str(round(discount_rate,2)) + '%\n'
   stringtoprint = stringtoprint + 'payout ratio: ' + str(round(payout_ratio,2)) + '%\n'
   stringtoprint = stringtoprint + 'tax rate: '+str(round(taxrate,2)) + '%\n'
   stringtoprint = stringtoprint + 'expected present value: '+str(round(expected_value,2)) +'\n'
   
   plotter.plot_countour(pe_points=pe_steps,
                         roe_points=roe_steps, 
                         presentvalues=presentvalues,
                         title=title,
                         directory=directory,
                         stringtoprint=stringtoprint)
   
   plotter.plot_wireframe(pe_points=pe_steps,
                          roe_points=roe_steps,
                          presentvalues=presentvalues,
                          currentprice=currentprice,
                          title=title,
                          directory=directory,
                          stringtoprint=stringtoprint)
   
   return {'pe_steps':pe_steps, 'roe_steps':roe_steps, 'presentvalues':presentvalues}