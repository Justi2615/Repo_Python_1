print('Siema')

while True:
    age = int(input('Ile masz lat?   '))
    if age > 18:
        print(f'Więc masz {age} lat.')
        print('Jesteś już pełnoletni.')
        break
    elif age < 0:
        print('Błędny wiek. Spróbuj jeszcze raz.')
    else:
        print(f'Więc masz {age} lat.')
        print(f'Będziesz dorosły za {18 - age} lat.')
        break

print('Dalsza część programu.')