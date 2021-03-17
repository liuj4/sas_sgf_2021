#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


# In[2]:


def gettickerdata(ticker):
    newdata = pdr.get_data_yahoo(ticker, start='1991-1-1', end='2020-12-31')
    newdata.to_csv('stock\\'+ticker+'.csv')


# In[3]:


def getalldata(tickerlist):
    for t in tickerlist:
        gettickerdata(t)


# In[5]:


tickerlist=['^DJI','^GSPC','^IXIC','^RUT',
            'XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY']
tickerlist=['SPY','QQQ','IWM',
            'EWA','EWC','EWD','EWG','EWH','EWI','EWJ','EWK','EWL','EWM','EWN','EWO',
            'EWP','EWQ','EWS','EWT','EWU','EWW','EWX','EWY','EWZ']
tickerlist=['CCIV','THBR','APXT','SSPK','CIIC','SRAC',
            'AAPL','MSFT','AMZN','GOOG','FB','TSLA','NVDA','PYPL','INTC','NFLX',
            'BRK-B','V','JPM','JNJ','WMT','MA','DIS','PG','UNH','HD']
getalldata(tickerlist)




