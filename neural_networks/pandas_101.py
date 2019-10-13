import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

'''
Pandas DataFrames
'''

# Read iris dataset from UCI database
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# check for null values
print(df.isnull().any())
# drop null values
df3 = df.dropna()
# replace null values with mean
df.sepal_length = df.sepal_length.fillna(df.sepal_length.mean())
print(df.head())
df.describe()

df2 = df.loc[df['sepal_length'] > 5.0]
print(df2)

sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue="class")
plt.show()

sns.distplot(df['petal_length'], kde=False)
plt.show()

df['petal_length'].plot.hist()
plt.show()

df.plot.box(title="Box Plot")
plt.show()


df2 = pd.DataFrame({'Day':[
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
]})

print(pd.get_dummies(df2))
