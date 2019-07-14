# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:15:14 2019

@author: Yong Keong
"""

This stock screener library is for quickly plotting the performance of a company across time.
If you observe that it is somewhat stable and 'predictable', you can try to extrapolate future results.

A full description of the algorithm and mathematics behind it is given
Refer to algorithm_description.txt.

So how do we use this code library? Let's dive in.

========= Manual steps =========

1. Let's say you like VISA. Go to morningstar. 
    Download the keyratios csv file from morningstar.

2. Go to the morningstar valuation page. 
    Copy the PB, PE and price-cashflow ratios into the csv.

3. Store the CSV into your /sample_data/raw/ folder.

4. Run generate_test_data.generate_csv_skeleton() without arguments.
    You should see a new file /sample_data/csv_skeleton_data.csv
    Rename the file to VISA_YEAR_condensed.csv
    Open this CSV. You should see a table format.
    
5. Open the morningstar csv. Copy the appropriate rows into the _condensed csv.
    Make sure the csv files format the data as numbers, not strings.
    Close the file, you are all set.
    
6. Before crunching the numbers, make sure the exchange rates are correct. 
===== End of manual steps ======
===== Generation of plots ======
1. To visualize a company's old parameters and stats, use the following function
    main_functions_wrapper.analyze_data(directory='', filename='', title='test company',plot=True)
    
    The arguments are pretty self explanatory. The stats (avg,std,max,min) will be printed.
    You will see a plot of the different parameters across the morningstar dataset.
    The function will spit out [data, stock_stats]
    <data> is time series data of the CSV file in a python dictionary form.
    <stock_stats> is a dictionary containing statistical numbers about PB, PE, ROE, payoutratios.
    
2. To predict the future, you can eyeball the figures to make future estimates.
    To guess the payout ratio, eyeball the history and read qualitative statements from management.
    To guess the PE ratio, take a look at statistical past.
    To guess the ROE going forward, eyeball the past statisics and read industry news, analysts.

3. Once you have the estimated performance figures, you need 3 more figures. 
    Dividend tax rate %:    30 (USA), 0 (Singapore), Not sure about the rest
    Discount rate %:        the rate you expect to be rewarded at
    Years to invest:        the number of years to hold this. 
                            Recommended is < half of the historical data
                            Projections futher than old data dont make a lot of sense

4. Plug in all the figures into this function
    main_functions_wrapper.project_data(data, stock_stats, 
                                        projectionyear=2019, 
                                        years2project=5, 
                                        title='test company',
                                        discount_rate=5,
                                        taxrate=0,
                                        directory='',plot=True)
    <data> and <stock_stats> are spit out by step 1. The end result will be a projection.
    The present value will be printed on the console as well as in the projection plots.
    
==== End of plot generation ====
=== Advanced analyst section ===
TODO: include documentation on how to sweep.
=== End of advanced analysts ===