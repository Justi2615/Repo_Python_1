lista_liczb = [3, 65, 43, 7, 54, 12, 13]
suma_liczb = 0
iloczyn_liczb = 1
suma_liczb_parzystych = 0
for liczba in lista_liczb:
    suma_liczb += liczba
    iloczyn_liczb *= liczba
    if liczba % 2 == 0:
        suma_liczb_parzystych += liczba
print(f'Suma liczb to: {suma_liczb}')
print(f'Iloczyn liczb to: {iloczyn_liczb}')
print(f'Suma liczb parzystych to: {suma_liczb_parzystych}')










