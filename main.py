#Mean Reversion Backtesting on options chain
import yfinance as yf
import pandas as pd

#fetch tesla ticker and options expy dates
tsla = yf.Ticker("TSLA")
tsla_expy = tsla.options
print(tsla_expy)