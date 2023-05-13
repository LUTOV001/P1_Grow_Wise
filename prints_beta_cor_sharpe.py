from Risk_Return_Analysis import *
from grow_wise_monte_carlo import *  
from risk_questions import 

def beta_cor_sharpe_print():

    print("Below is the list of high beta,medium beta and low beta stocks recommendation")
    #check the risk_return_analysis file to get (get_beta_data) # Risk_Return_Analysis
    high_beta,med_beta,low_beta=get_beta_data()
    beta_return(high_beta,med_beta,low_beta)

    print("Below is the list of highly correlated,medium correlated and low correlated stocks recommendation")
    #check the risk_return_analysis file to get (get_correlation_data) # Risk_Return_Analysis
    high_correlation_tickers,med_correlation_tickers,low_correlation_tickers=get_correlation_data()
    correlation_return(high_correlation_tickers,med_correlation_tickers,low_correlation_tickers)

    print("Below is the list of high risk adjusted return i.e sharpe ratio,medium return and low return stocks recommendation")
    #check the risk_return_analysis file to get (get_sharpe_data) # Risk_Return_Analysis
    high_sharpe_tickers,med_sharpe_tickers,low_sharpe_tickers=get_sharpe_data()
    sharpe_return(high_sharpe_tickers,med_sharpe_tickers,low_sharpe_tickers)