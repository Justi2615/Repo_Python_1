# Chcemy, aby program zwrócił nam informację, za ile lat będziemy pełnoletni.

wiek = int(input('Podaj wiek:   '))

print(f'Będziesz pełnoletni za {18 - wiek} lat')

# Chcemy napisać program, który pyta o zarobki, liczbę dzieci i zwierząt.
# Jeżeli dziecko to 800+, utrzymanie zwierzaka kosztuje 300 zł, to ile mamy pieniędzy na osobę ?

zarobki = float(input('Podaj zarobki:   '))
liczba_dzieci = int(input('Podaj liczbę dzieci:   '))
liczba_zwierzat = int(input('Podaj liczbę zwierząt:   '))

pieniadze_na_osobe = (zarobki + liczba_dzieci * 800 - liczba_zwierzat * 300) / (liczba_dzieci + 2)
print(f'Pieniądze na osobę wynoszą {pieniadze_na_osobe} zł')