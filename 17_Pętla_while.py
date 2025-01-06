x = 0
while x<5:
    print('Wykonuję kod')
    x += 1

print('koniec')

# Program, który przejdzie dalej tylko, gdy podamy poprawne hasło
passwd = '1234'
user_passwd = input('Podaj hasło:   ')
while user_passwd != passwd:
    print('Błędne hasło, spróbuj ponownie')
    user_passwd = input('Podaj hasło:   ')

print('Hasło poprawne, przejście dalej')

# passwd = '1234'
# user_passwd = input('Podaj hasło:   ')
# while user_passwd != passwd:
#     user_passwd = input('Podaj hasło:   ')
#
# print('Hasło poprawne, przejście dalej')


