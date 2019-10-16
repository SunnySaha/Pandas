import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv('data.csv')
x= data.iloc[:, :-1].values
y = data.iloc[:, 4].values
sns.heatmap(data.corr())
data.plot(kind = 'bar')
plt.show()

