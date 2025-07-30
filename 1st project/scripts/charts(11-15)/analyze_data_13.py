import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

covid_data = pd.read_csv('1st project/data/country_wise_latest.csv')

print(covid_data.head())


#13 - plot a histogram of 'New cases' distribution:
plt.figure(figsize=(10,8))
plt.title('New cases distribution')

sns.histplot(covid_data['New cases'], bins=30, kde=True, color='skyblue', edgecolor='black')
plt.xlabel('New Cases')
plt.ylabel('Number of Countries')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

plt.savefig('1st project/output/charts/histogram_for_new_cases_distribution.png')

plt.show()