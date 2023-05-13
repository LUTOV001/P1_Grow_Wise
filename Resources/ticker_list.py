# import csv
# from pathlib import Path


# tickers=['AAPL', 'ADBE', 'AFRM', 'AMD', 'AMZN', 'BABA', 'BIDU', 'COIN', 'COUR', 'CRM', 'CRWD', 'CSCO', 'DBX', 'DDOG', 'DOCU', 'FSLY', 'GOOGL', 'IBM', 'INTC', 'JD', 'LYFT', 'MDB', 'META', 'MSFT', 'NET', 'NFLX', 'NOW', 'NVDA', 'OKTA', 'ORCL', 'PATH', 'PLTR', 'PYPL', 'RBLX', 'SHOP', 'SNAP', 'SNOW', 'SPOT', 'SQ', 'TCEHY', 'TEAM', 'TSLA', 'TSM', 'TWLO', 'U', 'UBER', 'WDAY', 'ZI', 'ZM', 'ZS']

# with open('tech_tickers.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     for tick in tickers:
#         writer.writerow([tick])

# def tickers_load_file():
#      csvpath=Path(r'./Resources/tech_tickers.csv')
#      return tickers_load_csv(csvpath)

# def tickers_load_csv(csvpath):
#     """Reads the CSV file from path provided.

#     Args:
#         csvpath (Path): The csv file path.

#     Returns:
#         A list of lists that contains the rows of data from the CSV file.

#     """
#     with open(csvpath, "r") as csvfile:
#         data = {}
#         csvreader = csv.reader(csvfile, delimiter=",")

#         # Skip the CSV Header
#         next(csvreader)

#         # Read the CSV data
#         for row in csvreader:
#             data[row[0]]=row[:]
#     print(data)
#     return data

def ticker_list():
    tickers = ['AAPL', 'ADBE', 'AFRM', 'AMD', 'AMZN', 'BABA', 'BIDU', 'COIN', 'COUR', 'CRM', 'CRWD', 'CSCO', 'DBX', 'DDOG', 'DOCU', 'FSLY', 'GOOGL', 'IBM', 'INTC', 'JD', 'LYFT', 'MDB', 'META', 'MSFT', 'NET', 'NFLX', 'NOW', 'NVDA', 'OKTA', 'ORCL', 'PATH', 'PLTR', 'PYPL', 'RBLX', 'SHOP', 'SNAP', 'SNOW', 'SPOT', 'SQ', 'TCEHY', 'TEAM', 'TSLA', 'TSM', 'TWLO', 'U', 'UBER', 'WDAY', 'ZI', 'ZM', 'ZS']
    return tickers

# print(tickers_list())