import pandas as pd
financials_data = pd.read_csv('/content/Financial Statements.csv')
financials_data.head()

import matplotlib.pyplot as plt
revenue_trends = financials_data.groupby('Year')['Revenue'].sum()
plt.figure(figsize=(10, 6))
plt.plot(revenue_trends.index, revenue_trends.values, marker='o',
linestyle='-', color='b')
plt.title('Revenue Trends Over the Years', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Total Revenue (in millions)', fontsize=14)
plt.grid(True)
plt.show()

company_revenue = financials_data.pivot_table(values='Revenue', index='Year', columns='Company ')
company_revenue.plot(kind='bar', figsize=(12, 8))
plt.title('Revenue Comparison Across Companies', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Revenue (in millions)', fontsize=14)
legend = plt.legend(title='Company', loc='upper left')
plt.legend(title='Company', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(False)
plt.tight_layout()
plt.show()

print(financials_data.columns)

financials_data['Revenue Growth Rate (%)'] = financials_data.groupby('Company ')['Revenue'].pct_change() * 100
financials_data[['Year', 'Company ','Revenue', 'Revenue Growth Rate (%)']].dropna()

from matplotlib import pyplot as plt
_df_3.plot(kind='scatter', x='Year', y='Revenue', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

