#Importing all the libraries and dependencies.
import pandas as pd                     
import numpy as np
# import seaborn as sns
# import datetime as dt
import matplotlib.pyplot as plt
from MCForecastTools import MCSimulation
import yfinance as yf
from yahoo_fin.stock_info import get_data
import warnings
warnings.filterwarnings('ignore')
from Resources.ticker_list import ticker_list
from utilities.grab_current_date import *
import spy_data
import tickers_calculations 

# 50 tickers
daily_return_df, cumulative_returns, std_of_ticker_sorted, annualized_standard_deviation, annualized_average_return, annualized_sharpe_sorted = tickers_calculations.calculate_50_tickers()
daily_returns = tickers_calculations.daily_returns_50_tickers()

# SPY
spy_cumulative_returns, std_of_SPY500, annualized_standard_deviation_SPY500, annualized_average_return_SPY500 , annualized_sharpe_SPY500 = spy_data.spy_calculations()
daily_returns_SPY500 = spy_data.daily_returns_SPY500()
# Optimization 

rank_risk_Return={}
# Top 10%
for i in range(1, 16):
    rank_risk_Return[i] = 'High Volatility'
# Middle 20%
for i in range(16, 32):
    rank_risk_Return[i] = 'Medium Volatility'
# Bottom 20%
for i in range(32, 51):
    rank_risk_Return[i] = 'Low Volatility'

# add rank number to the index of std_devs series
ranked_std_dev = std_of_ticker_sorted.rank(ascending=False) 

# create a DataFrame from the ranked_std_dev series
std_dev_df = pd.DataFrame(ranked_std_dev, columns=['Rank'])

# add the corresponding ticker symbols to the DataFrame
std_dev_df['Ticker'] = std_of_ticker_sorted.index

# set the ticker column as the index
std_dev_df.set_index('Ticker', inplace=True)

# create a new column in the std_devs DataFrame to store the group
std_dev_df['Group'] = ranked_std_dev.apply(lambda x: rank_risk_Return.get(x, 'Unknown'))

# sort the std_devs_df DataFrame based on rank
#std_dev_df.sort_values(by=['Rank'], inplace=True)

### GROUPING ###

# create a dictionary to store the ranked tickers
ranked_tickers_std = {
    "Group 1": list(ranked_std_dev[ranked_std_dev <= 15].index),
    "Group 2": list(ranked_std_dev[(ranked_std_dev > 15) & (ranked_std_dev <= 31)].index),
    "Group 3": list(ranked_std_dev[ranked_std_dev > 31].index),
}
print('\n***Grouping Tickers by Beta***\n')
for item in ranked_tickers_std.items():
    print(f'{item}')
print('')
# print(ranked_tickers_std)

# This will output a dictionary with three keys, "Group 1", "Group 2", and "Group 3", 
# with the respective tickers for each group. 
# The stocks are grouped based on their rank, 
# where Group 1 has the highest volatility, 
# Group 2 has medium volatility, 
# and Group 3 has the lowest volatility.


Sharpe_rank_risk_Return={}
# Top 10%
for i in range(1, 16):
    Sharpe_rank_risk_Return[i] = 'High Return'
# Middle 20%
for i in range(16, 32):
    Sharpe_rank_risk_Return[i] = 'Medium Return'
# Bottom 20%
for i in range(32, 51):
    Sharpe_rank_risk_Return[i] = 'Low Return'

# add rank number to the index of sharpe_ratio series
ranked_sharpe_ratio = annualized_sharpe_sorted.rank(ascending=False) 
#print(ranked_std_dev)

# create a DataFrame from the ranked_sharpe_ratio series
sharpe_ratio_df = pd.DataFrame(ranked_sharpe_ratio, columns=['Rank'])
#print(sharpe_ratio_df)
# add the corresponding ticker symbols to the DataFrame
sharpe_ratio_df['Ticker'] = annualized_sharpe_sorted.index
#print(std_dev_df)
# set the ticker column as the index
sharpe_ratio_df.set_index('Ticker', inplace=True)

# create a new column in the sharpe ratio DataFrame to store the group
sharpe_ratio_df['Group'] = ranked_sharpe_ratio.apply(lambda x: Sharpe_rank_risk_Return.get(x, 'Unknown'))

# sort the sharpe_ratio_df DataFrame based on rank
sharpe_ratio_df.sort_values(by=['Rank'], inplace=True)

# creates a dictionary to store the ranked tickers
ranked_tickers_sharpe = {
    "Group 1": list(ranked_sharpe_ratio[ranked_sharpe_ratio <= 15].index),
    "Group 2": list(ranked_sharpe_ratio[(ranked_sharpe_ratio > 15) & (ranked_sharpe_ratio <= 31)].index),
    "Group 3": list(ranked_sharpe_ratio[ranked_sharpe_ratio > 31].index),
}
print('\n***Ranking Tickers by Sharpe Ratio***\n')
for item in ranked_tickers_sharpe.items():
    print(f'{item}')
print('')
# print(ranked_tickers_sharpe)

# This will output a dictionary with three keys, "Group 1", "Group 2", and "Group 3", 
# with the respective tickers for each group. 
# The stocks are grouped based on their rank, 
# where Group 1 has the highest return, 
# Group 2 has medium return, 
# and Group 3 has the lowest return.

# Calculates Covariance of all 50 stocks to compare it with variance of s&p500.
covariance_50stocks={}
for ticker in ticker_list():
    covariance_each_stock_with_SPY500= daily_return_df[ticker].cov(daily_returns_SPY500)
    covariance_50stocks[ticker]=covariance_each_stock_with_SPY500

# print(covariance_50stocks)

#Create DataFrame for all Tickers and covariance.
#pd.DataFrame(covariance_50stocks)
df_final = pd.DataFrame(covariance_50stocks.items())
df_final.columns = ['Ticker','Covariance']
# df_final.head()

#Calculates the variance of S&P500.
sp500_Var=daily_returns_SPY500.var()
# sp500_Var


#Calculate Correlation between each ticker with s&p500.
correlation_50stocks={}
for ticker in ticker_list():
    correlation_each_stock_with_SPY500= daily_return_df[ticker].corr(daily_returns_SPY500)
    correlation_50stocks[ticker]=correlation_each_stock_with_SPY500


#Calculates the beta based on the covariance of stocks compared to the market (S&P 500)
df_final['Beta'] = df_final['Covariance']/sp500_Var
df_final['Correlation']=correlation_50stocks.values()


# Optimization on the basis of beta.
#Sorting based on beta in descending order.
df_final_sorted_by_beta=df_final.sort_values(by=['Beta'],ascending=False)

# ranking them in descending order of beta.
df_final_sorted_by_beta['Rank'] = df_final_sorted_by_beta['Beta'].rank(ascending=False) 
# print(df_final_sorted_by_beta.head()) #DEBUG


#Grouping them based on rank.
#Adding new column "Sensitivity" based on criteria-
#Rank (1 to 15)= 'High Sensitivity'
#Rank (16 to 31)= 'Medium Sensitivity'
#Rank (32 to 50)= 'low Sensitivity'
df_final_sorted_by_beta['sensitivity'] = ''
df_final_sorted_by_beta.loc[df_final_sorted_by_beta['Rank']<16,'sensitivity'] = 'High Sensitivity'
df_final_sorted_by_beta.loc[(df_final_sorted_by_beta['Rank']>=16)&(df_final_sorted_by_beta['Rank']<32),'sensitivity'] = 'Medium Sensitivity'
df_final_sorted_by_beta.loc[df_final_sorted_by_beta['Rank']>=32,'sensitivity']='Low Sensitivity'


#Sorted the dataframe and rank them by beta.
# df_final_sorted_by_beta.tail(20) #DEBUG

# Optimization on the basis of Correlation.
#Sorting based on Correlation in descending order.
df_final_sorted_by_Correlation=df_final.sort_values(by=['Correlation'],ascending=False)

# ranking them in descending order of Correlation.
df_final_sorted_by_Correlation['Rank'] = df_final_sorted_by_Correlation['Correlation'].rank(ascending=False) 
# print(df_final_sorted_by_Correlation.head(10)) #DEBUG

#Grouping them based on rank.
#Adding new column "Correlation Type" based on criteria
df_final_sorted_by_Correlation['Correlation Type'] = ''
df_final_sorted_by_Correlation.loc[df_final_sorted_by_Correlation['Rank']<16,'Correlation Type'] = 'Highly Correlated'
df_final_sorted_by_Correlation.loc[(df_final_sorted_by_Correlation['Rank']>=16)&(df_final_sorted_by_Correlation['Rank']<32),'Correlation Type'] = 'Moderatly Correlated'
df_final_sorted_by_Correlation.loc[df_final_sorted_by_Correlation['Rank']>=32,'Correlation Type']='Less Correlated'
# df_final_sorted_by_Correlation #DEBUG 

# Stocks Recommandation on the basis of risk score.(max=50)
# Portfolio allocation based on three parameters:
def portfolio_recommandation(risk_score): # prints to risk_questions.your_risk_score()
    final_portfolio_recommend_list=[]

    if risk_score <=16:
        final_portfolio_recommend_list=df_final_sorted_by_Correlation['Ticker'].head().tolist() 
        for item in df_final_sorted_by_beta['Ticker'].tail().tolist():
            final_portfolio_recommend_list.append(item)

    elif risk_score >=17 and risk_score <32:
        final_portfolio_recommend_list=(sharpe_ratio_df.iloc[15:25].index.values.tolist())    
        for item in df_final_sorted_by_beta['Ticker'].iloc[15:25].tolist():
            final_portfolio_recommend_list.append(item)

    elif risk_score >=32:
        final_portfolio_recommend_list=sharpe_ratio_df.head().index.values.tolist()   
        for item in df_final_sorted_by_beta['Ticker'].head().tolist():
            final_portfolio_recommend_list.append(item)

    return final_portfolio_recommend_list

def get_beta_data():
    high_beta=[]
    med_beta=[]
    low_beta=[]

   #Assigning ranked beta data in a list.
    high_beta=df_final_sorted_by_beta['Ticker'].iloc[0:16].tolist() 
    med_beta=df_final_sorted_by_beta['Ticker'].iloc[16:32].tolist() 
    low_beta=df_final_sorted_by_beta['Ticker'].iloc[32:51].tolist() 
    print(high_beta) 
    print(med_beta) 
    print(low_beta)      
    
    return high_beta,med_beta,low_beta

def get_correlation_data():
    highly_correlated=[]
    med_correlated=[]
    low_correlated=[]

    #Assigning ranked correlated data in a list.
    highly_correlated=df_final_sorted_by_Correlation['Ticker'].iloc[0:16].tolist() 
    med_correlated=df_final_sorted_by_Correlation['Ticker'].iloc[16:32].tolist() 
    low_correlated=df_final_sorted_by_Correlation['Ticker'].iloc[32:51].tolist() 
    print(highly_correlated) 
    print(med_correlated) 
    print(low_correlated)      
    
    return highly_correlated,med_correlated,low_correlated

def get_sharpe_data():
    high_sharpe=[]
    med_sharpe=[]
    low_sharpe=[]

   #Assigning ranked sharpe return data in a list.
    high_sharpe=sharpe_ratio_df['Ticker'].iloc[0:16].tolist() 
    med_sharpe=sharpe_ratio_df['Ticker'].iloc[16:32].tolist() 
    low_sharpe=sharpe_ratio_df['Ticker'].iloc[32:51].tolist() 
    print(high_sharpe) 
    print(med_sharpe) 
    print(low_sharpe)      
    
    return high_sharpe,med_sharpe,low_sharpe