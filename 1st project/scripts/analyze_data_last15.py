import pandas as pd


covid_data = pd.read_csv('1st project/data/country_wise_latest.csv')

print(covid_data.head())


#16 - what is the total number of new cases globally?
x = covid_data['New cases'].sum()
print(x)


#17 - what is the average death rate across countries?
x = covid_data['Deaths / 100 Cases'].mean()
print(x)