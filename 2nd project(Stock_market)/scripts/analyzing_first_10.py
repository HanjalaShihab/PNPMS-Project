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


#7 - 