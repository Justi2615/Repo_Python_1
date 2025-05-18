import os
import time

print(os.getcwd())
os.chdir(r'C:\Users\Marian\Desktop')
print(os.getcwd())

print(os.environ['PATH'])
print(os.environ['OS'])

try:
    os.mkdir('test')
except FileExistsError:
    print('Plik już istnieje')

time.sleep(2)
os.rename('test', 'test2')
time.sleep(2)
os.rmdir('test2')

os.system('cmd /c "ipconfig /all >> info.txt"')