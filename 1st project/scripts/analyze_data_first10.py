import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


covid_data = pd.read_csv('1st project/data/country_wise_latest.csv')

print(covid_data.head())
print()


#1 - what is the total number of confirmed covid-19 cases worldwide?
x = covid_data['Confirmed'].sum()
print(x)
print()


#2 - which country has the highest number of confirmed cases:
x = covid_data.loc[covid_data['Confirmed'].idxmax()]
print(x)
print()


#3 - which country has the lowest number of confirmed cases:
x = covid_data.loc[covid_data['Confirmed'].idxmin()]
print(x)
print()


#4 - what is the total number of deaths worldwide?
x = covid_data['Deaths'].sum()
print(x)
print()


#5 - which country has the highest death toll?
x = covid_data.loc[covid_data['Deaths'].idxmax()]
print(x)
print()


#6 - which country has the highest number of recovery count?
x = covid_data.loc[covid_data['Recovered'].idxmax()]
print(x)


#7 - which country has the highest number of active cases?
x = covid_data.loc[covid_data['Active']]