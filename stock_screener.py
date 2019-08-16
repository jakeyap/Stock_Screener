# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:09:59 2018

@author: Yong Keong
"""
import main_functions_wrapper as main
'''
=========Key in parameters here==========
'''
estimated_roe = 11
estimated_pe = 4
estimated_payout_ratio = 25
dcf_rate = 10
div_taxrate = 30
currentprice = 178
years2project = 10
sampletitle = 'VISA_2019'
filename = sampletitle+'_condensed.csv'
directory = 'sample_data/'
'''
=========END of stock parameters=========
'''
'''
=========Key in plot parameters==========
'''
plot_1_prediction = True
plot_sweeps = True
bollinger_compensation = True
'''
=========END of plot parameters=========
'''

if __name__ == "__main__":
   # analyze data
   if plot_1_prediction:
      [data, stats] = main.analyze_data(directory=directory, filename=filename, title=sampletitle)
      # plug in some conservative estimates
      stats = main.modify_stock_stats(stock_stats=stats,
                         est_roe=estimated_roe,
                         est_pe=estimated_pe,
                         est_payout_ratio=estimated_payout_ratio)
      predictionyear = data['year'][-1] + 1

      main.project_data_by_roe(data=data, 
                   stock_stats=stats,
                   projectionyear=predictionyear,
                   years2project=years2project,
                   title=sampletitle,
                   discount_rate=dcf_rate,
                   taxrate=div_taxrate,
                   directory=directory)
   if plot_sweeps:
      sweepresolution=20
      prices = main.sweep_parameters_roe_and_pe(discount_rate=dcf_rate, 
                                       payout_ratio=estimated_payout_ratio, 
                                       currentprice=currentprice,
                                       directory=directory, 
                                       filename=filename, 
                                       title=sampletitle,
                                       resolution=sweepresolution, 
                                       bollinger_compensation=bollinger_compensation,
                                       projectionyear=predictionyear,
                                       taxrate=div_taxrate)
      
      #main.plotter.plot_countour(prices['pe_steps'],prices['roe_steps'],prices['presentvalues'])