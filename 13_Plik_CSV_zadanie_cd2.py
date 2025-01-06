with open ('rozliczenie.csv', 'r') as file1:
    content = file1.readlines()

for i in range(len(content)):
    content[i] = content[i].split(',')

#3. Ile osób zarabia powyżej 4000 ?
licznik = 0
for i in range(1, len(content)):
    if int(content[i][1])>4000:
        licznik += 1

print(f'Liczba osób zarabiających powyżej 4000 zł to: {licznik}')
