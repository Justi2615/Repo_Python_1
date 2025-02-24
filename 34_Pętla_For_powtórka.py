lista_imion = ['Zdzisław', 'Marianna', 'Stefan', 'Genowefa', 'Teodozja', 'Witold']

for imię in lista_imion:
    if imię[-1] == 'a':
        print(f'{imię} to imię żeńskie')
    else:
        print(f'{imię} to imię męskie')

