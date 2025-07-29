import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


covid_data = pd.read_csv('1st project/data/country_wise_latest.csv')

print(covid_data.head())


#what is the total number of confirmed covid-19 cases worldwide?
x = covid_data['Confirmed'].sum()
print(x)


#which country has the highest number of confirmed cases:
x = covid_data.loc[covid_data['Confirmed'].idxmax()]
print(x)
print()


#which country has the lowest number of confirmed cases:
x = covid_data.loc[covid_data['Confirmed'].idxmin()]
print(x)