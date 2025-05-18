import pandas as pd

df = pd.read_csv('plik.csv')
df_excel = pd.read_excel('plik.xslx', sheet_name='Arkusz1')

df.head()
df.head(10)
df.tail()
df.tail(10)

df.info()
df.describe()

df['nazwa kolumny']
df[['kolumna1'], ['kolumna2']]

df[df['kolumna'] == 'wartość']
df[df['kolumna'] > 10]
df[(df['kolumna1'] > 5) & (df['kolumna2'] == 'abc')]

df.loc[0:10, ['kolumna1'], ['kolumna2']]
df.iloc[0:10, 0:2]

df['kolumna_numeryczna'].sum()
df.sum()
df['kolumna'].count()
df.count()
df['kolumna_numeryczna'].mean()
df['kolumna_numeryczna'].median()
df['kolumna_numeryczna'].std()
df['kolumna_numeryczna'].unique()
df['kolumna_numeryczna'].nunique()

grupa = df.groupby('kolumna_kategoryczna')
grupa['kolumna_numeryczna'].mean()

df.groupby('kolumna_kategoryczna')['kolumna_numeryczna'].agg(['count', 'mean', 'sum'])

df['nowa_kolumna'] = df['kolumna1'] + df['kolumna2']

df.drop('kolumna_do_usunięcia', axis=1, inplace=True)

df.dropna(inplace=True)

df['kolumna'].fillna(0, inplace=True)

df.to_csv('nowy-plik.csv', index=False)
df.to_excel('nowy-plik.xlsx', sheet_name='Wyniki', index=False)