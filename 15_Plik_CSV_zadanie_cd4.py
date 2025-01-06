with open ('rozliczenie.csv', 'r') as file1:
    content = file1.readlines()

for i in range(len(content)):
    content[i] = content[i].split(',')

#5. Oblicz maksymalną ilość kolumn w pliku.

max_kolumn = 0
index = -1
for i in range(len(content)):
    if len(content[i]) > max_kolumn:
        max_kolumn = len(content[i])
        index = i

print(f'Maksymalna liczba kolumn w pliku wynosi: {max_kolumn} w linii {index+1}')