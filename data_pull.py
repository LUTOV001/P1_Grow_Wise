# import yfinance as yf
# from utilities.grab_current_date import *
# from risk_questions import *
# import sys

# # S&P500 data pulled from yfinance.
# def spy_data():
#     if call_question() != 0:
#         print('***Pulling S&P Data***')
#         data_spy = yf.download("SPY",start='2013-01-01', end=today_date(), progress=False)
#         print(data_spy)
#         return(data_spy)
#     else:
#         print('ERROR AT DATA PULL --- EXITING APPLICATION')
#         sys.exit()
    