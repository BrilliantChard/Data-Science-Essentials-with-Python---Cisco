import pandas as pd
import matplotlib.pyplot as plt


earth_layers = {
    'Layers': ['Crust', 'Mantle', 'Outer Core', 'Inner Core'],
    'Thickness': [40, 2900, 2200, 1230]
}

data = pd.DataFrame(earth_layers)

# Total sum of thickness
total_thickness = data['Thickness'].sum()

print(f'Total thickness of the Earth: {total_thickness} km')

# Dusplaying the Data
print(f'\nEarth layers data: \n{data}')

# Plotting the data

# 1. Plotting a bar chart

plt.figure(figsize=(8, 6))
plt.bar(data['Layers'], data['Thickness'], color=['brown', 'orange', 'yellow', 'red'])
plt.title('Thickness of Earth Layers')
plt.xlabel('Earth Layers')
plt.ylabel('Thickness (km)')
plt.show()

# 2. Plotting a Pie chart

plt.figure(figsize=(8, 6))
patches, texts, autotexts = plt.pie(data['Thickness'], labels=data['Layers'], autopct='%1.1f%%', colors=['brown', 'orange', 'yellow', 'red'])
plt.title('Proportion of Earth Layers by Thickness')
plt.legend(patches, data['Layers'], title='Earth Layers', loc='best')
plt.show()





