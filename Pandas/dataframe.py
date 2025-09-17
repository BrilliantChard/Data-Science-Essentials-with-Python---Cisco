import pandas as pd


# Create a DataFrame
data = pd.DataFrame()

data['color'] = ['red', 'blue', 'green', 'blue', 'red']
data['radius'] = [2, 4, 3, 10, 5]

# Show data
print(f'My data: \n{data}')

# Adding the Diameter column

data['diameter'] = data['radius'] * 2
print(f'\nMy data after adding diameter column: \n{data}')

# Smallest radius
min_radius = data['radius'].min()

# Adding up all the diameters
diameter_sum = data['diameter'].sum()

# Average radius
avg_radius = data['radius'].mean()

print(f'\nSmallest radius: {min_radius} \nTotal diameter: {diameter_sum} \nAverage radius: {avg_radius}')

# Accessing Rows
first_row = data.iloc[0]
print(f'\nFirst row of the data: \n{first_row}')












print(f'Shape of the data: {data.shape}')
no_of_rows = data.shape[0]
no_of_columns = data.shape[1]
print(f'Number of rows: {no_of_rows} \nNumber of columns: {no_of_columns}')


