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


#20 - what percentage of confirmed cases are active globally?
x = (covid_data['Active'].sum() / covid_data['Confirmed'].sum()) * 100
print(f"{x:.2f}%")
print()


#21 - what are the top 5 countries with the highest new case growth?(1 week % increase)
x = covid_data.sort_values(by= '1 week % increase', ascending= False)
y = x[['Country/Region', '1 week % increase']].head(5)
print(y)
print()


#22- which countries have zero new cases?
x = covid_data['New cases'] == 0
final = covid_data[x][['Country/Region', 'New cases']].values
print(final)
print()


#23 - how many countries belong to each WHO Region?
x = covid_data.groupby(['WHO Region'])['Country/Region'].count().sort_values(ascending= False)
print(x)


#24 - what is the relationship between new deaths and new cases(correlation)?
x = covid_data[['New deaths', 'New cases']]
print(x.corr())
print()


#25 - identify countries with more than 80% recovery rate?
x = covid_data['Recovered / 100 Cases'] > 80
final = covid_data[x][['Country/Region','Recovered / 100 Cases']].values.tolist()
print(final)