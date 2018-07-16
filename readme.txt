================================================
Author: Yap Yong Keong                  Date: 20180716
This folder is a project to try my hand at implementing a stock screener.
The end goal is simple.
To try to put in a table of stock financial data such as 
earnings, debt, growth, share count, stock price, dividends
and try to predict the future value by discounted cash flow.

The book titled Buffetology by Mary Buffet describes an algorithm.
    1. Are earnings predictable? Consistent or growing?
    2. Determine initial rate of return. EPS / price
    3. Determine per share growth rate
    4. Determine value of company relative to gov bonds
    5. Determine annual compounding rate
    6. Compare to gov bonds
    
So in our first file, we will do some regression on earnings.
We will do regression on total earnings & EPS.
================================================