# Logowanie do programu

# standard_username = 'Kamil'
# standard_passwd = '1234'
#
# username = input('Podaj nazwę użytkownika:   ')
# passwd = input('Podaj hasło:   ')
# while username != standard_username or passwd != standard_passwd:
#     print('Złe dane')
#     username = input('Podaj nazwę użytkownika:   ')
#     passwd = input('Podaj hasło:   ')
# print('Zalogowano')

# albo z dodatkową zmienną
standard_username = 'Kamil'
standard_passwd = '1234'
a = 0
username = input('Podaj nazwę użytkownika:   ')
passwd = input('Podaj hasło:   ')
while a == 0:
    if username == standard_username and passwd == standard_passwd:
        a = 1
    else:
        print('Złe dane')
        username = input('Podaj nazwę użytkownika:   ')
        passwd = input('Podaj hasło:   ')
print('Zalogowano')