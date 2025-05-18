import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('dane/weight-height.csv')

print(df.head(10))
print(df.Gender.value_counts())

df.Height *= 2.54
df.Weight /= 2.2
print(f'Po zmianie jednostek: \n{df.head(10)}')

# print('\nWykres pyplot')
# plt.hist(df.Weight, 50)
# plt.show()
#
# print('\nWykres seaborn')
# sns.histplot(df.Weight)
# plt.show()
#
# print('\nWykres pyplot dla mężczyzn')
# plt.hist(df.query('Gender=="Male"').Weight, 50)
#
# print('\nWykres pyplot dla kobiet')
# plt.hist(df.query('Gender=="Female"').Weight, 50)
# plt.show()

df = pd.get_dummies(df)
print(df.head(10))

del df['Gender_Male']
print(df.head(10))

df = df.rename(columns={'Gender_Female': 'If_Female'})
print(df.head(10))

model = LinearRegression()
model.fit(df[['Height', 'If_Female']], df['Weight'])

print(f'Współczynnik kierunkowy: {model.coef_}\nWyraz wolny: {model.intercept_}')

print('waga = wzrost * 1.07 - płeć * 8.8 - 102.5')

print(model.predict([[192, 0], [167, 1], [80, 1]]))