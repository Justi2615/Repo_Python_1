lista_zakupow = ['marchew', 'seler', 'majonez', 'chleb']
print(lista_zakupow)
print(lista_zakupow[2])
print(lista_zakupow[1:3])
print(lista_zakupow[1][:2])

# for i in range(len(lista_zakupow)):
#     print(lista_zakupow[i])

for produkt in lista_zakupow:
    print(produkt)

# Chcielibyśmy wypisać wszystkie elementy dłuższe niż 5 liter.
# for i in range(len(lista_zakupow)):
#     if len(lista_zakupow[i])>5:
#         print(f'Słowo dłuższe niż 5 liter: {lista_zakupow[i]}')

for produkt in lista_zakupow:
    if len(produkt)>5:
        print(f'Słowo dłuższe niż 5 liter: {produkt}')