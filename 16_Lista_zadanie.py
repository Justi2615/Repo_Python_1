# Tworzymy program, który powie nam, co trzeba kupić.
do_kupienia = ['marchew', 'chleb', 'masło', 'mleko']
w_domu = ['miód', 'chleb', 'mleko', 'pomidor', 'sok']

# for i in range(len(do_kupienia)):
#     print(do_kupienia[i])

# for produkt in do_kupienia:
#     print(produkt)

# Rozwiązanie nie najlepsze

# for produkt in do_kupienia:
#     for item in w_domu:
#         if produkt == item:
#             print(f'Nie kupuj {produkt}')
#         else:
#             print(f'Kup {produkt}')

# # Wypisze tylko produkty, które mamy
# for produkt in do_kupienia:
#     for item in w_domu:
#         if produkt == item:
#             print(f'Nie kupuj {produkt}')

# Rozwiązanie z dodatkową zmienną.

# for produkt in do_kupienia:
#     mam = False
#     for item in w_domu:
#         if produkt == item:
#             mam = True
#             print(f'Nie kupuj {produkt}')
#     if mam == False:
#         print(f'Kup {produkt}')


for produkt in do_kupienia:
    if produkt in w_domu:
        print(f'Masz w domu: {produkt}')
    else:
        print(f'Kup: {produkt}')

# for produkt in do_kupienia:
#     if produkt not in w_domu:
#         print(f'Kup: {produkt}')
#     else:
#         print(f'Masz w domu: {produkt}')




