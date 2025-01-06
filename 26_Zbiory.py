NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma = zbior1 | zbior2
# przeciecie = zbior1 & zbior2          część wspólna
# roznica = zbior1 - zbior2
# roznica_symetryczna = zbior1 ^ zbior2

# Zadanie: Ile osób chorowało w ostatnim roku na Krzykach ?

print(f'W ostatnim roku na Krzykach chorowało {len(chorzy_rok & krzyki)} osób')
print(chorzy_rok & krzyki)

# Ile osób mieszka w sumie w centrum i na krzykach ?

print(f'W sumie w Centrum i na Krzykach mieszka {len(centrum | krzyki)} osób')
print(centrum | krzyki)

# Sprawdźmy poprawność danych
print('\nPoprawność danych')

# Kaźdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku
print(f'Osoby, które chorowały w ostatnim miesiącu, ale nie chorowały w ostatnim roku to: {chorzy_miesiac - chorzy_rok}')
if len(chorzy_miesiac - chorzy_rok) == 0:
    print('Ok')

# Nikt nie powinien mieszkać jednocześnie w Centrum i na Krzykach. Jeżeli są takie osoby, to trzeba je usunąć.
# Zróbmy program, który zapyta, skąd usuwamy te osoby i to robi.
# print(f'Osoby, które mieszkają i w Centrum i na Krzykach to: {centrum & krzyki}, ilość osób: {len(centrum & krzyki)}')
# zbior = input('Z którego zbioru chcesz usunąć powtarzające się osoby: Centrum, Krzyki czy oba ?   \n')
# nowe_centrum = centrum
# nowe_krzyki = krzyki
# if zbior == 'Centrum' or zbior == 'centrum':
#     nowe_centrum = centrum - krzyki
# if zbior == 'Krzyki' or zbior == 'krzyki':
#     nowe_krzyki = krzyki - centrum
# if zbior == 'Oba' or zbior == 'oba':
#     nowe_centrum = centrum - krzyki
#     nowe_krzyki = krzyki - centrum
#
# print(f'Osoby, które mieszkają i w Centrum i na Krzykach to: {nowe_centrum & nowe_krzyki}, ilość osób: {len(nowe_centrum & nowe_krzyki)}')
# print(f'Osoby, które mieszkają w Centrum to: {nowe_centrum}')
# print(f'Osoby, które mieszkają na Krzykach to: {nowe_krzyki}')

# duplikaty = krzyki & centrum
# if len(duplikaty) != 0:
#     print('\nZnaleziono duplikaty - usuwam')
#     krzyki = krzyki - duplikaty
# if len(krzyki & centrum) == 0:
#     print('OK, brak duplikatów')
