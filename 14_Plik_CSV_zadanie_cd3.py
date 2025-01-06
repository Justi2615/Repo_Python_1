with open ('rozliczenie.csv', 'r') as file1:
    content = file1.readlines()

for i in range(len(content)):
    content[i] = content[i].split(',')

#4. Ile kobiet jest na macierzyńskim ?

# ile_na_macierz = 0
# for i in range(1, len(content)):
#     if content[i][3] == 'k' and (content[i][4] == 't\n' or content[i][4] == 't'):
#         ile_na_macierz += 1

# ile_na_macierz = 0
# for i in range(1, len(content)):
#     if content[i][3] == 'k':
#         if content[i][4] == 't\n' or content[i][4] == 't':
#             ile_na_macierz += 1

ile_na_macierz = 0
for i in range(1, len(content)):
    if content[i][3] == 'k':
        content[i][4] = content[i][4].replace('\n', '')
        if content[i][4][0].lower() == 't':
            ile_na_macierz += 1

print(f'Liczba kobiet na macierzyńskim to: {ile_na_macierz}')