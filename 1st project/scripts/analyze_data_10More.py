import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

covid_data = pd.read_csv('1st project/data/country_wise_latest.csv')


#11 - plot a bar chart of 10 countries with the most confirmed cases:
top10 = covid_data.sort_values(by= 'Confirmed', ascending= False).head(10)

plt.figure(figsize=(12,8))
plt.title('Top 10 countries with most confirmed cases')

sns.barplot(x = 'Country/Region', y = 'Confirmed', data= top10,  palette="Reds_r")

plt.xlabel("Countries")
plt.ylabel("Confirmed")

plt.tight_layout()

plt.savefig("1st project/output/charts/top10_confirmed_cases_seaborn.png")

plt.show()