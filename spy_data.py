import yfinance as yf
from utilities.grab_current_date import *
import numpy as np
# import pandas as pd                     
from yahoo_fin.stock_info import get_data

### SPY
#S&P500 data pulled from yfinance.

# Calculates the daily return for S&P500 on adjusted closing price by using percentage change.
def daily_returns_SPY500():
    print('***Pulling S&P Data***')
    data_spy = yf.download("SPY",start='2013-01-01', end=today_date())
    daily_returns_SPY500={}
    daily_returns_SPY500 = data_spy['Adj Close'].pct_change().dropna()
    daily_returns_SPY500.name='Adj Close'
    #print(daily_returns_SPY500)
    return(daily_returns_SPY500)

def spy_calculations():
    #Calculates Cumulative Returns bu using daily return series.
    spy_cumulative_returns=(1 + daily_returns_SPY500()).cumprod()-1
    # cumulative_returns.head() # prints

    # Standard Deviation of S&P500.
    std_of_SPY500=daily_returns_SPY500().std()
    # std_of_SPY500 # prints

    # Annualized standard deviation (252 trading days) of S&P500.
    annualized_standard_deviation_SPY500 = std_of_SPY500* np.sqrt(252)
    # annualized_standard_deviation_SPY500 # prints

    # Calculates the annual average return data for the for S&P500 by 252 (the number of trading days in the year)
    trading_Days=252
    annualized_average_return_SPY500=daily_returns_SPY500().mean()*trading_Days

    # Calculates Shape Ratio
    # risk_free_rate=0
    annualized_sharpe_SPY500 = annualized_average_return_SPY500 / annualized_standard_deviation_SPY500
    # annualized_sharpe_SPY500
    return spy_cumulative_returns, std_of_SPY500, annualized_standard_deviation_SPY500, annualized_average_return_SPY500 , annualized_sharpe_SPY500