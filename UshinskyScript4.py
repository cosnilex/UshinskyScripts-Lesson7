#!/usr/bin/python3

try:
    import os
except ModuleNotFoundError:
    print(f'Модуль с таким именем не найден')
try:
    print(f'{os.name}')
    print(f'{os.getlogin()}')
    print(f'{os.listdir(path=".")}')
except NameError:
    print(f'Ошибка выполнения')
    