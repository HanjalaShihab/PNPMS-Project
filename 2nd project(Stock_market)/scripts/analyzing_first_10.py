import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

stock = pd.read_csv('2nd project(Stock_market)/data/AAPL_Mock_2020_2023.csv', index_col='Date', parse_dates= True)

print(stock.head())
print()

#what is the shape and summary of the dataset?
shape = stock.shape
print(shape)
print()

summary = stock.describe()
print(summary)
print()