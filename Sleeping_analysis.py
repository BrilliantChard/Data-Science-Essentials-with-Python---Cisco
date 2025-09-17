import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset

data = pd.read_csv('Sleep and health dataset.csv')

print(f'The columns in the dataset: \n{data.columns.to_list()}')

print(f'Few details of the data: \n{data.head()}')

print(f'Information about the dataset: {data.info()}')

print(f'Statistical summary of the dataset: \n{data.describe()}')

# Exploratory Data Analysis (EDA)

# Settiing the Person ID as index

data = data.set_index('Person ID')
print(data.head())

# Gender distribution
print(data['Gender'].value_counts())

# Occuoation distribution
print(data['Occupation'].value_counts())

#Visualizing the distribution of Age

plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=30, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Missing Values Analysis

print(f'Misisng values in each column: \n{data.isnull().sum()}')

# Print rows that contain ANY missing values
print(data.isna().any(axis=1))
# Print rows that contain ALL missing values
print(data.isna().all(axis=1))




