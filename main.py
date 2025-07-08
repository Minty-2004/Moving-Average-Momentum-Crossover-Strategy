import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

#Download financial data
ticker = str(input("Please enter the ticker symbol you would like to analyse (for example, the ticker for Apple would be 'AAPL'): ")) #Choose any ticker
span = str(input("What date would you like to start the analysis from? Please use the format YYYY-MM-DD: "))
data = yf.download(ticker, start=span, end=datetime.today().strftime('%Y-%m-%d'))

if data.empty:
    print("Could not download data for the specified ticker and date range. Please check the ticker symbol and start date.")
else:
    data['MA10'] = data['Close'].rolling(10).mean()
    data['MA50'] = data['Close'].rolling(50).mean()

    data['MA50Y'] = data['MA50'].shift(1)

    data['SignMA50'] = np.where(data['MA50'] - data['MA50Y'] > 0,1,0)
    data['10v50'] = np.where(data['MA10']>data['MA50'],1,0)
    data['Shares'] = np.where(data['SignMA50']+data['10v50']==2,1,0)
    data['CloseDiff'] = data['Close'].diff()
    data['Profits'] = data['Shares'] * data['CloseDiff']
    data = data.dropna()

    if data.empty:
        print("DataFrame is empty after dropping NaN values. Cannot proceed with calculations and plotting.")
    else:
        data['BuyHoldWealth'] = data['CloseDiff'].cumsum()
        data['StrategicWealth'] = data['Profits'].cumsum()

        data['StrategicWealth'].plot(label='Positive Momentum Strategy')
        data['BuyHoldWealth'].plot(label='Buy & Hold')
        plt.legend()
        plt.title(f'Total returns of {ticker} with the Positive 50-day Momentum Strategy are {round(data['StrategicWealth'].iloc[-1],2)}, compared to Buy & Hold returns of {round(data['BuyHoldWealth'].iloc[-1],2)}')
        plt.show()