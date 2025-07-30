import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

covid_data = pd.read_csv('1st project/data/country_wise_latest.csv')

print(covid_data.head())

#12 - plot a bar chart of top 10 countries with the most deaths:
x = covid_data.sort_values(by= 'Deaths', ascending= False).head(10)
print(x)


plt.figure(figsize=(10,8))
plt.title('Top 10 countries with most deaths')

sns.barplot(x = 'Country/Region', y= 'Deaths', data= x)

plt.xlabel('Country')
plt.ylabel('Deaths')

plt.tight_layout()

plt.savefig('1st project/output/charts/top10_death_cases.png')

plt.show()