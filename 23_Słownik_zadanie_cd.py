zakupy = {'chleb': 4, 'maslo': 1, 'sok': 2, 'jablko': 5}

ceny_lidl = {'chleb': 2.5, 'maslo': 9, 'sok': 4.7, 'jablko': 5, 'kurczak': 9.98}
ceny_aldi = {'chleb': 6, 'maslo': 7, 'sok': 0.99, 'jablko': 7, 'kurczak': 13}
ceny_dino = {'chleb': 4, 'maslo': 4, 'sok': 9.99, 'jablko': 0, 'kurczak': 14}

# Gdzie najtaniej ?

# for produkt in zakupy:
#     print(produkt)

# for produkt in zakupy.keys():
#     print(produkt)

# for produkt in zakupy.values():
#     print(produkt)

total_lidl = 0
total_aldi = 0
total_dino = 0

for produkt in zakupy:
    print(f'Cena {produkt} w Lidlu wynosi: {ceny_lidl[produkt]}')
    print(f'Cena {produkt} w Aldi wynosi: {ceny_aldi[produkt]}')
    print(f'Cena {produkt} w Dino wynosi: {ceny_dino[produkt]}')
    total_lidl += ceny_lidl[produkt] * zakupy[produkt]
    total_aldi += ceny_aldi[produkt] * zakupy[produkt]
    total_dino += ceny_dino[produkt] * zakupy[produkt]

print(f'Cena zakupów w Lidlu wynosi: {total_lidl}')
print(f'Cena zakupów w Aldi wynosi: {total_aldi}')
print(f'Cena zakupów w Dino wynosi: {total_dino}')
