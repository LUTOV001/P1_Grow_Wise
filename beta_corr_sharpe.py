import Risk_Return_Analysis
import grow_wise_monte_carlo
import risk_questions
import matplotlib.pyplot as plt
import hvplot


def plot_beta_corr_sharpe():
    print("Below is the list of high beta,medium beta and low beta stocks recommendation")
    #check the risk_return_analysis file to get (get_beta_data) # Risk_Return_Analysis
    high_beta,med_beta,low_beta=Risk_Return_Analysis.get_beta_data()
    grow_wise_monte_carlo.beta_return(high_beta,med_beta,low_beta)

    print("Below is the list of highly correlated,medium correlated and low correlated stocks recommendation")
    #check the risk_return_analysis file to get (get_correlation_data) # Risk_Return_Analysis
    high_correlation_tickers,med_correlation_tickers,low_correlation_tickers=Risk_Return_Analysis.get_correlation_data()
    grow_wise_monte_carlo.correlation_return(high_correlation_tickers,med_correlation_tickers,low_correlation_tickers)

    print("Below is the list of high risk adjusted return i.e sharpe ratio,medium return and low return stocks recommendation")
    #check the risk_return_analysis file to get (get_sharpe_data) # Risk_Return_Analysis
    high_sharpe_tickers,med_sharpe_tickers,low_sharpe_tickers=Risk_Return_Analysis.get_sharpe_data()
    grow_wise_monte_carlo.sharpe_return(high_sharpe_tickers,med_sharpe_tickers,low_sharpe_tickers)

# def beta_correlation_sharpe():
#     if risk_questions.call_question() <= 16:
#         print(f"Below is the list of conservative recommendations; based on low")




# def beta_cor_sharpe_print():
#     if risk_questions.call_question() <= 16:
#         print('Below is a Conservative list of stocks with low beta')
#         low_beta = get_beta_data()
#         beta_return(low_beta)
#         print('And a list of tickers with High Correlation to the market')
#         high_correlation_tickers = get_correlation_data()
#         correlation_return(high_correlation_tickers)


