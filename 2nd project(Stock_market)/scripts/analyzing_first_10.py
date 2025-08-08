import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

stock = pd.read_csv('2nd project(Stock_market)/data/AAPL_Mock_2020_2023.csv', parse_dates= ['Date'])

print(stock.head())
print()

#1 - what is the shape and summary of the dataset?
shape = stock.shape
print(shape)
print()

summary = stock.describe()
print(summary)
print()


#2 - what is the range of dates in the dataset?
min = stock.index.min()
max = stock.index.max()
print(min, "-", max)
print()


#3 - what are the top 5 highest closing prices?
top5HighClosingPrice = stock.sort_values(by= 'Close', ascending= False).head()
print(top5HighClosingPrice[['Date','Close']])
print()


#4 - what are the top 5 lowest closing prices?
top5LowClosingPrice = stock.sort_values(by= 'Close', ascending= True).head()
print(top5LowClosingPrice)
print()


#5 - On which date was the highest trading volume recorded?
highestVolume = stock.sort_values(by= 'Volume', ascending= False).head(1)
print(highestVolume[['Date', 'Volume']])
print()


#6 - what is the average closing price over the entire dataset?
avg = stock['Close'].mean()
print(f"{avg:.2f}")
print()


#7 - what is the median opening price?
avg = stock['Open'].median()
print(f"{avg:.2f}")
print()


#8 - What is the standard deviation of the closing prices?
std = stock['Close'].std()
print(f"{std:.2f}")
print()


#9 - What was the stock price change (percentage) from the first to the last date?
first_close = stock['Close'].iloc[0]
last_close = stock['Close'].iloc[-1]


pct_change = ((last_close - first_close) / first_close) * 100

print(f"Stock price changed by {pct_change:.2f}% from {stock['Date'].iloc[0]} to {stock['Date'].iloc[-1]}")
print()


#10 - What is the daily return (percentage) for each day?
stock['Daily return(%)'] = stock['Close'].pct_change() * 100
print(stock[['Date', 'Close', 'Daily return(%)']].head())
print()


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