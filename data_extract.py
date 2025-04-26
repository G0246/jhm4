from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta

ticker_symbol = 'AAPL'

data = yf.download(ticker_symbol, start='2020-01-01', end='2024-04-25')
data.to_csv('AAPL_historical_data.csv')