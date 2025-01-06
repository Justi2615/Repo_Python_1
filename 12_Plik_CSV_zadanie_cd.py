with open ('rozliczenie.csv', 'r') as file1:
    content = file1.readlines()

for i in range(len(content)):
    content[i] = content[i].split(',')

#2. Oblicz średnią wypłatę

suma_wyplat = 0
for i in range(1, len(content)):
    # content[i][1] = int(content[i][1])
    suma_wyplat += int(content[i][1])

print(f'Suma wypłat wynosi: {suma_wyplat}')
print(f'Średnia wypłata to: {suma_wyplat/(len(content)-1)}')

print(f'Liczba wierszy to: {len(content)}')
print(f'Liczba kolumn to: {len(content[0])}')


