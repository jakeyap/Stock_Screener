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

estimated_roe = 20
estimated_pe = 25
estimated_payout_ratio = 20
dcf_rate = 6
div_taxrate = 30

currentyear = 2019
years2project = 10
sampletitle = 'VISA_2019'
filename = sampletitle+'_condensed.csv'
directory = 'sample_data/'

def analyze_data(directory='', filename='', title='test company'):
   '''
   A wrapper function to generate summarized stock stats and show it graphically
   Arguments:
      directory: the raw file directory
      filename: uh huh
      title: string to be saved into the plot
   Returns: [stats, data]
      stats: a dictionary containing _min _max _avg _std of roe pe_ratio payout_ratio pb_ratio 
      data: a dictionary of the whole stock data
   '''
   if (filename==''): # no filename given, use generated fake data
      data = generate_test_data.generate()
   else:
      data = extractor.read_csv2data(directory, filename)

   # Show the min, max, avg, std of the PE, PB, ROE, payout_ratio
   print('Showing stats')
   stock_stats = analyser.analyze_all_data(data,showstats=True)
   
   hist_roe = stock_stats['roe_avg']
   hist_pe = stock_stats['pe_ratio_avg']
   stringtoprint = 'Historical ROE mean: '+str(round(hist_roe,2)) + '\n'
   stringtoprint = stringtoprint + 'Historical PE mean: '+str(round(hist_pe,2))
   # Plot the old data, save it
   plotter.plot_full_dataset(title=title+' data', directory=directory, data=data,annotate_string=stringtoprint)
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

def project_data(data, stock_stats, projectionyear=2019, years2project=5, title='test company'):
   '''
   A wrapper function to do prediction of a stock N number of years later
   '''
   new_data = predictor.modify_dataset_multi_year(data=data, predicted_stats=stock_stats, years=years2project)
   presentvalue = predictor.dcf_calculator(year=currentyear,
                                  data=new_data,
                                  discount_rate=dcf_rate,
                                  taxrate=div_taxrate)
   
   stringtoprint = 'Long term ROE: ' + str(estimated_roe) +'\n'
   stringtoprint = stringtoprint + 'Estimated PE:  ' + str(estimated_pe) + '\n'
   stringtoprint = stringtoprint + 'Discount rate: ' + str(round(dcf_rate,2)) + '%\n'
   stringtoprint = stringtoprint + 'Present value: '+str(presentvalue)
   
   plotter.plot_full_dataset(title=title+' predictions',
                             data=new_data, 
                             directory=directory, 
                             projectionyear=projectionyear,
                             annotate_string=stringtoprint)
   print(stringtoprint)
   return