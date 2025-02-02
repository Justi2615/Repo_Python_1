import pandas as pd

df = pd.read_csv('Dane/diabetes.csv')
print(df)
print(type(df))
print(f'Ilość danych: {df.shape}, liczba kolumn: {df.shape[1]}, liczba wierszy: {df.shape[0]}')

# print(df.to_string())
print(df.head(3).to_string())

print(df.describe())