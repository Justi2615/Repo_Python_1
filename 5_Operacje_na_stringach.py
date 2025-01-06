napis = input('Napisz coś:   ')
print(napis)
print(napis[0])
print(napis[3])
print(napis[3:7])
print(napis[-1])
print(napis[-2])

print(f'Długość napisu to: {len(napis)}')

for i in range(len(napis)):
    print(napis[i])

for i in range(len(napis)):
    print(f'Znak {i+1} to: {napis[i]}')
    if napis[i] == 'a':
        print(f'Znalazłem literę a na pozycji {i + 1}')

# Pętla, która, gdy znajdzie spację, dzieli to, co wpiszemy na dwa słowa.
imie_i_nazwisko = input('Wpisz imię i nazwisko:   ')
for i in range(len(imie_i_nazwisko)):
    if imie_i_nazwisko[i] == ' ':
        print(f'Twoje imię to: {imie_i_nazwisko[0:i]}')
        print(f'Twoje nazwisko to: {imie_i_nazwisko[i+1:len(imie_i_nazwisko)]}')