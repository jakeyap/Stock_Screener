================================================
Author: Yap Yong Keong                  Date: 2018 Jul 16
This folder is a project to try my hand at implementing a stock screener.
The end goal is simple.
To try to put in a table of stock financial data such as 
earnings, debt, growth, share count, stock price, dividends
and try to predict the future value by discounted cash flow.

The book titled Buffetology by Mary Buffet describes an algorithm.
    1. Are earnings predictable? Consistent or growing?
    2. Determine initial rate of return. EPS / price
    3. Determine per share earnings growth rate
    4. Determine value of company relative to gov bonds
    5. Determine the best/worst cases stock price using historical PE
    6. Determine annual return compounding rate
    7. Is the company in serious debt? ( LTDebt + STDebt ) / Equity    
    
So in our first file, we will do some regression on earnings.
We will do regression on total earnings & EPS. Will predict earnings 10Y from now
================================================

Author: Yap Yong Keong                  Date: 2019 Jul 8
Changed the approach so far. Not doing regression on earnings anymore.
Instead, plot past data of 
   EPS
   ROE
   PE_ratio
   PB_ratio
   free cash flow per share (fcfps)
   dividend
   numberofshares
   payout_ratio

Using the historical ROE averages, use it to estimate future book value.

1. Estimate EPS_1 = (avg ROE) x bookvalue_0
2. Estimate dividends_1 = EPS_1 x (avg payout_ratio)
3. Estimate bookvalue_1 = (EPS_1 - div_1) + bookvalue_0
4. Estimate stockprice_1 = EPS_1 x (avg PE)

Iterate for some number of years, usually 5
So far, the steps to grab raw data is manual download from Morningstar
Copy the row/cols manually into a clean format.