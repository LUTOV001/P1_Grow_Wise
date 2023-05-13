import yfinance as yf
from utilities.grab_current_date import *
import numpy as np
import pandas as pd                     
from yahoo_fin.stock_info import get_data
from Resources.ticker_list import ticker_list


### 50 tech stocks
#50 tickers pulled from yfinance.

def daily_returns_50_tickers():
    tickers = ticker_list() # List of 50 stocks/tickers
    # Calculates Daily return of all 50 stocks and Cleans the data by dropping nan.
    daily_returns={}
    print('***Calculating Daily returns of all 50 stocks***') # Cleans the data by dropping nan
    for ticker in tickers:
        data = yf.download(ticker,start='2013-01-01', end=today_date())
        daily_return = data['Adj Close'].pct_change().dropna()
        daily_returns[ticker]=daily_return
        #print(daily_returns)
    return daily_returns

def calculate_50_tickers(daily_return_df, cumulative_returns, std_of_ticker_sorted, annualized_standard_deviation, annualized_average_return, annualized_sharpe_sorted):
    # Creates a dataframe of daily return on tickers.
    daily_return_df=pd.DataFrame(daily_returns_50_tickers())

    # Calculates Cumulative Returns bu using daily return dataframe.
    cumulative_returns=(1+daily_return_df).cumprod()-1
    # cumulative_returns.head()


    # Calculates and sorts the standard deviation for all 50 stocks.
    std_of_ticker=daily_return_df.std()
    std_of_ticker_sorted=std_of_ticker.sort_values(ascending=False) # Sorts largest to smallest.
    # std_of_ticker_sorted


    # Calculate and sort the annualized standard deviation (252 trading days) of all 50 stocks.
    annualized_standard_deviation = std_of_ticker* np.sqrt(252)
    annualized_standard_deviation.sort_values(ascending=False, inplace=True)
    # annualized_standard_deviation.sort_values(ascending=False).head() # Reviews the annualized std dev. sorted from highest to lowest.


    # Calculates the annual average return data for the for 50 tickers.

    trading_Days=252 # the number of trading days in the year
    annualized_average_return=daily_return_df.mean()*trading_Days
    annualized_average_return.sort_values(ascending=False, inplace=True)
    # annualized_average_return.sort_values(ascending=False).head() # Reviews the annual average returns sorted from highest to lowest.


    # Calculates the annualized Sharpe Ratios for each of the 50 Stocks.
    #risk_free_rate=0 # tf is this?
    annualized_sharpe = annualized_average_return / annualized_standard_deviation
    annualized_sharpe_sorted=annualized_sharpe.sort_values(ascending=False, inplace=True) # Sharpe ratios sorted highest to lowest
    # annualized_sharpe_sorted
    # type(annualized_sharpe_sorted)
    return daily_return_df, cumulative_returns, std_of_ticker_sorted, annualized_standard_deviation, annualized_average_return, annualized_sharpe_sorted

# print(daily_returns_50_tickers())
# print(calculate_50_tickers())