import streamlit as st
import pandas as pd
import yfinance  as yf 

st.write("""    
#Simple stock Price APP
Shown are the stock closing price and volume of Google!

     """)

# define the ticker symbol
tickerSymbol = 'GOOGL'

# get data on this ticker

tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerof=tickerData.history(period='1d',start='2010-5-31',end='2020-5-31')

st.write("""
## Closing Price""")
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.line_chart(tickerof.Close)
st.line_chart(tickerof.Volume)
