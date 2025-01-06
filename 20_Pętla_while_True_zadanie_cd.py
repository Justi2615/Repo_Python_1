# Program losuje liczbę, użytkownik zgaduje tę liczbę, a program informuje, czy za mało, czy za dużo, czy ok

# Wersja Kamila

# liczba = 7
# while True:
#     liczba_użytkownika = int(input('Podaj liczbę:   '))
#     if liczba_użytkownika > liczba:
#         print('Za dużo')
#     elif liczba_użytkownika < liczba:
#         print('Za mało')
#     else:
#         print('Ok')
#         break

# Wersja Kamila z losową liczbą

# import random
# liczba = random.randint(0, 10000)
# while True:
#     liczba_użytkownika = int(input('Podaj liczbę:   '))
#     if liczba_użytkownika > liczba:
#         print('Za dużo')
#     elif liczba_użytkownika < liczba:
#         print('Za mało')
#     else:
#         print('Ok')
#         break

# Liczba 9999 daje nam dostęp do trybu tajnego

# liczba = 7
# while True:
#     liczba_użytkownika = int(input('Podaj liczbę:   '))
#     if liczba_użytkownika == 9999:
#         print('Tryb tajny')
#         passwd = input('Podaj hasło:   ')
#         if passwd == 'Merito':
#             break
#     elif liczba_użytkownika > liczba:
#         print('Za dużo')
#     elif liczba_użytkownika < liczba:
#         print('Za mało')
#     else:
#         break
# print('Ok')

# import random
# liczba = random.randint(0, 10000)
# liczba_użytkownika = int(input('Podaj liczbę:   '))
# while True:
#     if liczba_użytkownika == liczba:
#         break
#     if liczba_użytkownika > liczba:
#         print('Za dużo')
#     if liczba_użytkownika < liczba:
#         print('Za mało')
#     liczba_użytkownika = int(input('Podaj liczbę:   '))
# print('Prawidłowa liczba, brawo')

# Niech program nam powie, jeżeli pomyliliśmy się o więcej niż 10

# import random
# liczba = random.randint(0, 10000)
# liczba_użytkownika = int(input('Podaj liczbę:   '))
# while True:
#     if liczba_użytkownika == liczba:
#         break
#     if liczba_użytkownika > (liczba + 10):
#         print('Za dużo o więcej niż 10')
#     if liczba_użytkownika < (liczba - 10):
#         print('Za mało o więcej niż 10')
#     if liczba < liczba_użytkownika <= (liczba + 10):
#         print('Za dużo (mniej niż 10)')
#     if (liczba - 10) < liczba_użytkownika < liczba:
#         print('Za mało (mniej niż 10)')
#     liczba_użytkownika = int(input('Podaj liczbę:   '))
# print('Prawidłowa liczba, brawo')

# Licznik prób

# import random
# liczba = random.randint(0, 10000)
# próba = 1
# print(f'Próba {próba}')
# liczba_użytkownika = int(input('Podaj liczbę:   '))
# while True:
#     if liczba_użytkownika == liczba:
#         break
#     if liczba_użytkownika > (liczba + 10):
#         print('Za dużo o więcej niż 10')
#     if liczba_użytkownika < (liczba - 10):
#         print('Za mało o więcej niż 10')
#     if liczba < liczba_użytkownika <= (liczba + 10):
#         print('Za dużo (mniej niż 10)')
#     if (liczba - 10) < liczba_użytkownika < liczba:
#         print('Za mało (mniej niż 10)')
#     próba += 1
#     print(f'Próba {próba}')
#     liczba_użytkownika = int(input('Podaj liczbę:   '))
# print('Prawidłowa liczba, brawo')
# print(f'Próba {próba}')

# Magiczne słowo merito pozwala nam uzyskać liczbę bez zgadywania

# import random
# liczba = random.randint(0, 10000)
# próba = 1
# magic_word = 'Merito'
# print(f'Próba {próba}')
# liczba_użytkownika = int(input('Podaj liczbę:   '))
# while True:
#     if liczba_użytkownika == liczba:
#         break
#     if liczba_użytkownika > (liczba + 10):
#         print('Za dużo o więcej niż 10')
#     if liczba_użytkownika < (liczba - 10):
#         print('Za mało o więcej niż 10')
#     if liczba < liczba_użytkownika <= (liczba + 10):
#         print('Za dużo (mniej niż 10)')
#     if (liczba - 10) < liczba_użytkownika < liczba:
#         print('Za mało (mniej niż 10)')
#     próba += 1
#     print(f'Próba {próba}')
#     liczba_użytkownika = int(input('Podaj liczbę:   '))
# print('Prawidłowa liczba, brawo')
# print(f'Próba {próba}')