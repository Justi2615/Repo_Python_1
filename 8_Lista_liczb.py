lista_liczb = [3, 65, 43, 7, 54, 12, 13]
suma_liczb = 0
for i in range(len(lista_liczb)):
    #suma_liczb = suma_liczb + lista_liczb[i]
    suma_liczb += lista_liczb[i]

print(f'Suma liczb to: {suma_liczb}')

iloczyn_liczb = 1
for i in range(len(lista_liczb)):
    iloczyn_liczb *= lista_liczb[i]

print(f'Iloczyn liczb to: {iloczyn_liczb}')

suma_liczb_parzystych = 0
for i in range(len(lista_liczb)):
    if lista_liczb[i] % 2 == 0:
        suma_liczb_parzystych += lista_liczb[i]

print(f'Suma liczb parzystych to: {suma_liczb_parzystych}')