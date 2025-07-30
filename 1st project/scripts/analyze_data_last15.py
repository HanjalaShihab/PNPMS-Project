import pandas as pd


covid_data = pd.read_csv('1st project/data/country_wise_latest.csv')

print(covid_data.head())
print()

#16 - what is the total number of new cases globally?
x = covid_data['New cases'].sum()
print(x)
print()


#17 - what is the average death rate across countries?
x = covid_data['Deaths / 100 Cases'].mean()
print(x)
print()


#18 - which WHO Region has the highest total number of confirmed cases?
x = covid_data.groupby(['WHO Region'])['Confirmed'].sum().idxmax()
print(x)
print()


#19 - what is the recovery rate of Bangladesh?
x = covid_data[covid_data['Country/Region'] == "Bangladesh"]['Recovered / 100 Cases'].values[0]
print(f"{x}%")
print()
