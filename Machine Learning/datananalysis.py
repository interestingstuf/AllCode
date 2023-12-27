import pandas as pd

data=pd.read_csv("/Users/desktop/Library/Mobile Documents/com~apple~CloudDocs/Code 2/ML/seaborn-data-master/iris.csv")
"""
print(data)
print(data.info())
print(data.shape)
print(data.head(20))
print(data.tail(20))
print(data.describe())
"""
corr_matrix=data.corr()
import seaborn as sns
import matplotlib.pyplot as plt
plt.subplots(figsize=(10,8))
sns.heatmap(corr_matrix,annot=True)
plt.show()
