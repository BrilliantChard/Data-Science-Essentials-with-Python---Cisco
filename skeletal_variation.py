import pandas as pd
import matplotlib.pyplot as plt

adult_data = pd.read_csv('adult.csv')
print(f'Few details of the data: \n{adult_data.head()}')

bird_data = pd.read_csv('bird.csv')
print(f'\nFew details of the bird data: \n{bird_data.head()}')

mammal_data = pd.read_csv('mammal.csv')
print(f'\nFew details of the mammal data: \n{mammal_data.head()}')


# Neck Bones

adult_neck_bones = adult_data.query("region == 'neck'")
print(f'\nHuman Neck bones: \n{adult_neck_bones}')

mammal_neck_bones = mammal_data['neck_vertebrae']
print(f'\nMammal neck bones: \n{mammal_neck_bones}')

bird_neck_bones = bird_data['neck_vertebrae']
print(f'\nBird neck bones: \n{bird_neck_bones}')


# Neck bone Plotings

counts = bird_data['neck_vertebrae'].value_counts().sort_index()

plt.figure(figsize=(8, 6))
plt.bar(counts.index, counts.values, color='skyblue', alpha=0.7, label='Birds')
plt.title('Neck Bones Comparison')
plt.xlabel('Bone')
plt.ylabel('Count of Birds')
plt.legend()
plt.show()


