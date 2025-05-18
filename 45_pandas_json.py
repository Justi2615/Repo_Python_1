import pandas as pd

df = pd.read_json('Dane/dane.json')
print(df.head())

mlodsi_niz_30 = df[df["wiek"] < 30]
print("\nOsoby młodsze niż 30 lat:")
print(mlodsi_niz_30)

df['wiek_za_5_lat'] = df['wiek'] + 5
print('\nDane z dodaną kolumną wiek_za_5_lat:')
print(df)

sredni_wiek = df['wiek'].mean()
print(f'\nŚredni wiek wynosi: {sredni_wiek}')

df_sorted = df.sort_values('wiek', ascending=False)
print('\nDane posortowane po wieku malejąco:')
print(df_sorted)

df.to_json('Dane_po_obróbce/dane.json', orient='records', indent = 4)