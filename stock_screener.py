# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:09:59 2018

@author: Yong Keong
"""
import main_functions_wrapper as main
'''
=========Key in parameters here==========
'''
currentprice = 58
estimated_roe = 23
estimated_pe = 14
estimated_payout_ratio = 38
dcf_rate = 12
div_taxrate = 30
years2project = 10
sampletitle = 'INTC_2021'
filename = sampletitle+'_condensed.csv'
directory = 'sample_data/'
std_multiplier = 2
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
        #hard_code_pe = {}
        #hard_code_pe['pe_ratio_avg'] = 13
        #hard_code_pe['pe_ratio_std'] = 1.5
        hard_code_pe = None
        prices = main.sweep_parameters_roe_and_pe(discount_rate=dcf_rate, 
                                                  payout_ratio=estimated_payout_ratio, 
                                                  currentprice=currentprice,
                                                  directory=directory, 
                                                  filename=filename, 
                                                  title=sampletitle,
                                                  resolution=sweepresolution, 
                                                  bollinger_compensation=bollinger_compensation,
                                                  projectionyear=predictionyear,
                                                  taxrate=div_taxrate,
                                                  std_multiplier=std_multiplier,
                                                  years2project=years2project,
                                                  hard_code_pe=hard_code_pe)
      
        #main.plotter.plot_countour(prices['pe_steps'],prices['roe_steps'],prices['presentvalues'])