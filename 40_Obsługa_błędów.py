age = int(input('Ile masz lat?   '))
if age <= 0:
    raise ValueError('Wiek musi być dodatni')