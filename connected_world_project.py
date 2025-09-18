import pandas as pd
import matplotlib.pyplot as plt


internet = pd.read_csv('world-internet-users.csv')
print(f'Few details of the data: \n{internet.head()}')

population = pd.read_csv('world_population.csv')
print(f'\nFew details of the population data: \n{population.head()}')

# The year the intenet users crossed the 10 Million mark
internet_10_million = internet.query("internet_users > 100e6").iloc[0]['year']
print(f"The year the internet users crossed the 10 Million mark: {internet_10_million}")

# Total years of internet use
total_years_of_internet_use = 2025 - internet['year'].min()
print(f'Total years of internet use: {total_years_of_internet_use}')


# Combining the two datasets
combined_data = internet.merge(population, on='year', how='left')
print(f'\nCombined data: \n{combined_data}')


# Drop columns with missing values
combined_data.dropna(inplace=True)
print(f'\nCombined data after dropping missing values: \n{combined_data}')

# Percentage of population using the internet
combined_data['Percentage'] = combined_data.eval('internet_users / population * 100').round(2)
print(f'\nCombined data with percentage of population using the internet: \n{combined_data}')


print('\nPercentage greater than or equal to 50 percent: \n', combined_data.query('Percentage >= 50'))

# Plotting the percentage of population using the internet over the years
plt.figure(figsize=(8, 6))
plt.bar(combined_data['year'], combined_data['Percentage'], color='skyblue', alpha=0.7)
plt.title('Percentage of Population Using the Internet Over Years')
plt.xlabel('Year')
plt.ylabel('Percentage of Population Using the Internet')
plt.show()






