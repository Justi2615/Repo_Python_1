liczba = 2.54675675
print(round(liczba, 2))

# def przywitanie():
#     print('Siema')
#
# przywitanie()
# przywitanie()

def przywitanie(imie):
    print(f'Siema {imie}')

przywitanie('Marek')
przywitanie('Zdzisław')

def pole_trojkata(a, h):
    pole = a * h / 2
    return pole

print(pole_trojkata(3, 7))

def welcome(name, age):
    if age < 18:
        print(f'Hi {name}')
    elif name[-1] == 'a':
        print(f'Hello Ms {name}')
    else:
        print(f'Hello Mr {name}')

welcome('Marian', 34)
welcome('Anna', 34)
welcome('Zdzisław', 14)
welcome('Ilona', 14)

# def create_mail(name, age):
#     if age < 18:
#         print('Nie można utworzyć maila dla osób poniżej 18 roku życia')
#         return ''
#     else:
#         if name[-1] == 'a':
#             mail = 'Ms.' + name + '@.onet.pl'
#         else:
#             mail = 'Mr.' + name + '@.onet.pl'
#         return mail
#
# print(create_mail('Marian', 34))
# print(create_mail('Anna', 34))
# print(create_mail('Zdzisław', 14))
# print(create_mail('Ilona', 14))

# def create_mail(name, age):
#     if age < 18:
#         print('Nie można utworzyć maila dla osób poniżej 18 roku życia')
#         return ''
#     if name[-1] == 'a':
#         mail = 'Ms.' + name + '@.onet.pl'
#     else:
#         mail = 'Mr.' + name + '@.onet.pl'
#     return mail
#
# print(create_mail('Marian', 34))
# print(create_mail('Anna', 34))
# print(create_mail('Zdzisław', 14))
# print(create_mail('Ilona', 14))

def create_mail(name, age):
    if age < 18:
        return 'Nie można utworzyć maila dla osób poniżej 18 roku życia'
    else:
        if name[-1] == 'a':
            return 'Ms.' + name + '@.onet.pl'
        else:
            return 'Mr.' + name + '@.onet.pl'

print(create_mail('Marian', 34))
print(create_mail('Anna', 34))
print(create_mail('Zdzisław', 14))
print(create_mail('Ilona', 14))
