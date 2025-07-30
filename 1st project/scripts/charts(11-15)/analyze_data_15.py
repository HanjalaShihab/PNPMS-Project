import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

covid_data = pd.read_csv('1st project/data/country_wise_latest.csv')

print(covid_data.head())


#15 - plot a heatmap showing correlation between all numerical columns:
numerical_data = covid_data.select_dtypes(include=['number'])
print(numerical_data)

corr_matrix = numerical_data.corr()
print(corr_matrix)


plt.figure(figsize=(12,10))
plt.title('Showing correlation between all numerical columns')

sns.heatmap(data= corr_matrix, annot= True)

plt.tight_layout()
plt.savefig('1st project/output/charts/correlation_between_numerical_numbers')

plt.show()