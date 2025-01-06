lista_imion = ['Kamil', 'Ewa', 'Monika', 'Grzegorz']

# Program, który wypisze osobno imiona męskie i żeńskie
# print('Imiona męskie to:')
# for i in range(len(lista_imion)):
#     if lista_imion[i][-1] != 'a':
#         print(lista_imion[i])

print('Imiona męskie to:')
for imie in lista_imion:
    if imie[-1] != 'a':
        print(imie)

# print('Imiona żeńskie to:')
# for i in range(len(lista_imion)):
#     if lista_imion[i][-1] == 'a':
#         print(lista_imion[i])

# print('Imiona żeńskie to:')
# for i in lista_imion:
#     if i[-1] == 'a':
#         print(i)

print('Imiona żeńskie to:')
for imie in lista_imion:
    if imie[-1] == 'a':
        print(imie)


