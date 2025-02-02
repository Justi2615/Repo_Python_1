import pandas as pd
from sklearn.linear_model import LinearRegression

df0 = pd.read_csv('weight-height.csv', delimiter=';')

df = df0.copy()

print(df)
print(type(df))

# print(df.describe())

df.Height *= 2.54
df.Weight /= 2.2

# print(df)
print(df.head(3))

df = pd.get_dummies(df)
print(df.head(3))

del df['Gender_Male']
print(df.head(3))

df = df.rename(columns={'Gender_Female': 'If_Female'})
print(df.head(3))

# Machine Learning
model = LinearRegression()
model.fit(df[['Height', 'If_Female']], df['Weight'])
print(model.coef_)
print(model.intercept_)

print(f'Weight = Height * {model.coef_[0]} + If_Female * {model.coef_[1]} + {model.intercept_}')