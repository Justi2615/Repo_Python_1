# Stwórz bazę użytkowników, gdzie każdy użytkównik ma mieć imię, nazwisko i wiek.
# Baza to lista, a użytkownik to słownik.

emp1 = {'imie': 'Anna', 'nazwisko': 'Kowalska', 'wiek': 18}
emp2 = {'imie': 'Karol', 'nazwisko': 'Nowak', 'wiek': 15}

user_database = [emp1, emp2]

print(user_database[1]['nazwisko'])

for user in user_database:
    user['email'] = user['imie'] + '.' + user['nazwisko'] + '@merito.com'
    print(user['email'])

print(user_database)

sredni_wiek = 0
suma_wieku = 0
for user in user_database:
    suma_wieku += user['wiek']
print(suma_wieku)
sredni_wiek = suma_wieku / len(user_database)

print(f'Średnik wiek wynosi {sredni_wiek}')