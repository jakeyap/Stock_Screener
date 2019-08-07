# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:22:37 2019

@author: Yong Keong
"""

import pandas as pd
import bs4 
from selenium import webdriver 

url = 'https://www.morningstar.com/stocks/xnas/ba/quote.html'

browser = webdriver.Chrome()
browser.get(url)

html = browser.page_source

soup = bs4.BeautifulSoup(html,'html.parser')

price = soup.find('div', {'id':'message-box-price'})
price2 = price.text.strip()
print(price2)

browser.close()