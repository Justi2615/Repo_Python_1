import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df0 = pd.read_csv('weight-height.csv', delimiter=';')

df = df0.copy()

print(df)
print(type(df))

# print(df.describe())

df.Height *= 2.54
df.Weight /= 2.2

# print(df)
print(df.head(3))

print('\nWykres')
sns.histplot(df.query('Gender=="Male"').Weight)
sns.histplot(df.query('Gender=="Female"').Weight)
plt.show()

df = pd.get_dummies(df)
print(df.head(3))

del df['Gender_Male']
print(df.head(3))

df = df.rename(columns={'Gender_Female': 'If_Female'})
print(df.head(3))