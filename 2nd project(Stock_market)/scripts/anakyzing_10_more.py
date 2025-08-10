import pandas as pd


stock = pd.read_csv('2nd project(Stock_market)/data/AAPL_Mock_2020_2023.csv', parse_dates= ['Date'])


#11 - Calculate the 7-day moving average of closing prices
stock['7 day moving avg'] = stock['Close'].rolling(window=(7)).mean()
print(stock[['Date','Close','7 day moving avg']].head(10))  #first 7 days will be empty as the first moving avg starts after 6th day
print()


#12 - Calculate the 30-day moving average of closing prices
stock['30 day moving avg'] = stock['Close'].rolling(window=(30)).mean()
print(stock[['Date', 'Close', '30 day moving avg']].head(15))
print()


#13 -  Which days had the closing price higher than the 30-day moving average?
x = stock.dropna()
closeHigher = x[x['Close'] > x['30 day moving avg']]
print(closeHigher[['Date', 'Close', '30 day moving avg']].head(10))

