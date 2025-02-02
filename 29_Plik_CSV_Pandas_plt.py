import pandas as pd
import matplotlib.pyplot as plt

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
plt.hist(df.Weight, 50)
plt.show()

plt.hist(df.query('Gender=="Male"').Weight, 50)
#plt.show()

plt.hist(df.query('Gender=="Female"').Weight, 50)
plt.show()