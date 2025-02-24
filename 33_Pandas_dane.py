import pandas as pd
import numpy as np

df = pd.read_csv('Dane/diabetes.csv')
print(df)
print(type(df))
print(f'Ilość danych: {df.shape}, liczba kolumn: {df.shape[1]}, liczba wierszy: {df.shape[0]}')

# print(df.to_string())
print(df.head(3).to_string())

# print(df.describe())
# print(df.describe().to_string())
print(df.describe().T.to_string())

print(df.isna().sum())

# Wszędzie, gdzie są zera lub brak wartości - wpisać średnią (bez zer)

# df['bmi'] += 1000
# df['nowa testowa'] = df['bmi'] / df['glucose'] - 50 * df.shape[1]
#
# df['bmi'] = df['bmi'].replace(0, np.nan)

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi', 'diabetespedigreefunction', 'age']:
    df[col].replace(0, np.nan, inplace=True)
    mean_ = df[col].mean()
    df[col].replace(np.nan, mean_, inplace=True)

print('Po czyszczeniu danych')
print(df.describe().T.to_string())
print(df.isna().sum())

df.to_csv(r'Dane_po_obróbce/cukrzyca.csv', sep=';', index=False)
