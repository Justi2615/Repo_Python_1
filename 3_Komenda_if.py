# Chcemy, aby program zwrócił nam informację, za ile lat będziemy pełnoletni,
# jeżeli nie jesteśmy jeszcze pełnoletni.

wiek = int(input('Podaj wiek:   '))
if wiek<18:
    print(f'Masz {wiek} lat')
    print(f'Będziesz pełnoletni za {18 - wiek} lat')
else:
    print('Jesteś już pełnoletni')

print('Koniec programu')

# Program, który sprawdza, czy podane hasło jest właściwe, a następnie wpuszcza do systemu.

correct_password = 1234
password = int(input('Podaj hasło:   '))
if password != correct_password:
    print('Błędne hasło, brak dostępu do systemu')
else:
    print('Prawidłowe hasło')
    print('Wejście do systemu')

print('Koniec programu')
