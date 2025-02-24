print('Siema')

age = input('Ile masz lat?   ')

try:
    age = int(age)
except:
    print('Przyjmuję wiek 10 lat')
    age = 10

print(f'Będziesz dorosły za {18 - age} lat.')