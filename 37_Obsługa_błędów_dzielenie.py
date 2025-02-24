while True:
    try:
        a = int(input('Podaj dzielną:   '))
        b = int(input('Podaj dzielnik:   '))
        result = a / b
        break
    except:
        print('Zła wartość - jeszcze raz')

print(result)
print('Dalej')