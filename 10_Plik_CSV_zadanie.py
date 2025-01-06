# 1. Odczyt pliku CSV z zapisem poszczególnych pól.

with open ('rozliczenie.csv', 'r') as file1:
    # content = file1.read()
    # print(content)
    # content = file1.read(5)
    # print(content)
    # content = file1.readline()
    # print(content)
    content = file1.readlines()
    print(content)

print(content[3])

# Chcemy podzielić wszystkie linie według przecinków, aby wyodrębnić różne informacje zawarte w pliku.

for i in range(len(content)):
    print('przed:', content[i])
    content[i] = content[i].split(',')
    print('po:', content[i])

print(content)
print(content[5])
print(content[5][2])
print(content[0][2][3:10])

print('Koniec części pierwszej\ni już')
