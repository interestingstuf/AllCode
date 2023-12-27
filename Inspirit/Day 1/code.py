import pandas as pd
import os

car_data=pd.read_csv('/Users/desktop/Downloads/car_dekho.csv')

import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x='Age', y='Kms_Driven', data= car_data)
plt.show()
sns.catplot(x = 'Transmission', y = 'Selling_Price', data = car_data, kind = 'swarm', s = 2)
plt.show()