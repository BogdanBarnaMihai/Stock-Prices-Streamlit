import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.title("Stock Closing Prices Over Time")

st.sidebar.header("Select Stock and Date Range")

tickers = ['SPY', 'GLD', 'AAPL', 'VTI', 'QQQ']
ticker = st.sidebar.selectbox("Choose a Stock Ticker", tickers)

start_date = st.sidebar.date_input("Start Date", datetime.today() - timedelta(days=2*365))
end_date = st.sidebar.date_input("End Date", datetime.today())

data = yf.download(ticker, start=start_date, end=end_date)

st.subheader(f"Stock Data for {ticker}")
st.write(data[['Close']])

plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label=ticker, color='black')  # Plot the stock's closing price

plt.title(f"{ticker} Closing Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.legend()

st.pyplot(plt)
