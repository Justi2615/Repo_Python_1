try:
    a = int(input('Podaj dzielną:   '))
    b = int(input('Podaj dzielnik:   '))
    result = a / b
    print(result)
    print('Piesek'[6])
except ValueError:
    print('Nie da się przekształcić danej wejściowej na int')
except IndexError:
    print('Za daleko w indexach')
except ZeroDivisionError:
    print('Dzielenie przez 0')
    raise

print('Dalej')