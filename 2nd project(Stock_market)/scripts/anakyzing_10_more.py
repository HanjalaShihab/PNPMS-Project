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
print()


#14 - On how many days did the stock close higher than it opened?
days_higher_close = (stock['Close'] > stock['Open']).sum()
print("Number of days stock closed higher than it opened:", days_higher_close)
print()


#15 - On how many days did the stock close lower than it opened?
days_lower_close = (stock['Close'] < stock['Open']).sum()
print("Number of days stock closed lower than it opened", days_lower_close)
print()


#16 - What is the rolling 7-day standard deviation (volatility)?
stock['7 day rolling std'] = stock['Close'].rolling(window= 7).std()
print(stock[['Date', 'Close', '7 day rolling std']].head())
print()


#17 - Identify the top 5 most volatile days based on daily price range (High - Low)?
stock['Daily range'] = stock['High'] - stock['Low']
top5 = stock.sort_values(by = 'Daily range', ascending= False).head()
print()


#18 - What is the correlation between volume and closing price?
correlation = stock['Volume'].corr(stock['Close'])
print(f"{correlation:.4f}")
print()


#19 - What is the maximum drawdown during the period?
cumulative_max = stock['Close'].cummax()
drawdown = (stock['Close'] - cumulative_max) / cumulative_max
max_drawdown = drawdown.min() * 100 

print(f"Maximum drawdown: {max_drawdown:.2f}%")
print()


#20 - What is the average daily return and standard deviation of daily return?
stock['Daily return'] = stock['Close'].pct_change()

daily_return_avg = stock['Daily return'].mean()
daily_return_std = stock['Daily return'].std()

print(f"Daily return average: {daily_return_avg:.2f}")
print(f"Daily return standard deviation: {daily_return_std:.2f}")
print()


#21 - What is the average closing price per month?
stock['Date'] = pd.to_datetime(stock['Date'])

monthly_avg_close = stock.groupby(stock['Date'].dt.to_period('M'))['Close'].mean()

print(monthly_avg_close)


