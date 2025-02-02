print('Siema')

age = int(input('Ile masz lat?   '))

if age > 18:
    print(f'Więc masz {age} lat.')
    print('Jesteś już pełnoletni.')
elif age < 0:
    print('Błędny wiek.')
else:
    print(f'Więc masz {age} lat.')
    print(f'Będziesz dorosły za {18 - age} lat.')