import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

covid_data = pd.read_csv('1st project/data/country_wise_latest.csv')

print(covid_data.head())


#14 - plot a boxplot of 'Confirmed' cases grouped by WHO Region:
x  = covid_data['WHO Region'].head(10)
print(x)


plt.figure(figsize=(9,6))
plt.title('confirmed cases grouped by WHO Region')

sns.boxplot(x='WHO Region', y='Confirmed', data=covid_data)

plt.tight_layout()
plt.savefig('1st project/output/charts/boxplot_confirmed cases grouped by WHO Region')

plt.show()