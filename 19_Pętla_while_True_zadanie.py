# Logowanie do programu z hasłem serwisowym
standard_username = 'Kamil'
standard_passwd = '1234'
service_passwd = 'service'

username = input('Podaj nazwę użytkownika:   ')
passwd = input('Podaj hasło:   ')
while True:
    if username == standard_username and passwd == standard_passwd:
        break
    elif passwd == service_passwd:
        break
    print('Złe dane')
    username = input('Podaj nazwę użytkownika:   ')
    passwd = input('Podaj hasło:   ')
print('Zalogowano')