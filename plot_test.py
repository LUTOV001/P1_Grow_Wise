# #!/usr/bin/env python
# # coding: utf-8

# # In[2]:


# import pandas as pd
# import yfinance as yf
# from yahoo_fin.stock_info import get_data 
# from MCForecastTools import MCSimulation
# import warnings
# warnings.filterwarnings('ignore')
# from Resources.ticker_list import ticker_list
# from utilities.grab_current_date import *
# import seaborn as sns
# # import webbrowser
# # from risk_questions import call_question

# # requires python 3.9 min


# #GLOBAL_VARIABLES
# # define investment amount
# investment_amount = 100000
# #List of 50 stocks/tickers
# # tickers=['AAPL', 'ADBE', 'AFRM', 'AMD', 'AMZN', 'BABA', 'BIDU', 'COIN', 'COUR', 'CRM', 'CRWD', 'CSCO', 'DBX', 'DDOG', 'DOCU', 'FSLY', 'GOOGL', 'IBM', 'INTC', 'JD', 'LYFT', 'MDB', 'META', 'MSFT', 'NET', 'NFLX', 'NOW', 'NVDA', 'OKTA', 'ORCL', 'PATH', 'PLTR', 'PYPL', 'RBLX', 'SHOP', 'SNAP', 'SNOW', 'SPOT', 'SQ', 'TCEHY', 'TEAM', 'TSLA', 'TSM', 'TWLO', 'U', 'UBER', 'WDAY', 'ZI', 'ZM', 'ZS']
# tickers = ticker_list()

# # In[4]:


# #List of 50 stocks/tickers
# # tickers = ["AAPL", "GOOGL", "AMZN", "META","TSM","MSFT", "TSLA", "NVDA", "PYPL", "INTC", "AMD", "IBM", "CSCO", "ORCL", "CRM", "ADBE", "ZM", "SQ", "DOCU", "NFLX", "SNAP", "SPOT", "DBX", "UBER", "LYFT", "WDAY", "NOW", "TEAM", "SHOP", "TWLO", "ZS", "OKTA", "MDB", "CRWD", "NET", "FSLY", "DDOG", "SNOW", "PLTR", "U", "RBLX", "AFRM", "PATH", "COUR", "COIN", "BIDU", "JD", "BABA", "TCEHY", "ZI"]

# # fetch historical data for each ticker grouping
# ticker_data = yf.download(tickers, start="2013-01-01", end=today_date())
# prices_df = ticker_data

# # display the resulting DataFrame
# prices_df


# # In[5]:


# # calculate daily returns for ticker data in prices DataFrame 
# daily_returns = prices_df["Close"].pct_change()

# # format daily returns DataFrame to make usable with MCForecastTools
# daily_returns.columns = pd.MultiIndex.from_product([daily_returns.columns, ["daily_return"]])
# daily_returns=daily_returns.swaplevel(axis=1).dropna()

# # display resulting DataFrame
# daily_returns


# # In[6]:


# # concatenate ticker DataFrame with Daily Returns DataFrame
# prices_df = pd.concat([prices_df, daily_returns], axis=1, join="inner")

# # display resulting DataFrame
# ax = prices_df.plot

import matplotlib.pyplot as plt
import random
import numpy as np
import seaborn as sns

runs = 1000000 # global variable

def steadystate(): # generates random array
    p=0.88
    Cout=4700000000
    LambdaAER=0.72
    Vol=44.5
    Depo=0.42
    Uptime=0.1
    Effic=0.38
    Recirc=4.3
    x = random.randint(86900000,2230000000000)
    conc = ((p*Cout*LambdaAER)+(x/Vol))/(LambdaAER+Depo+(Uptime*Effic*Recirc))
    return conc

results = np.array([steadystate() for _ in range(runs)]) # creates array using for loop
print(results) 

# creates plot from results and shows via new window
ax = sns.distplot(results,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')
plt.show()