try:
    import modul as mod
except ModuleNotFoundError:
    print(f'Модуль с таким именем не найден')
try:
    res = mod.inbytes(['Александр', 'Владимир', 'Дмитрий'])
    print(f'{res}')
    print(f'{mod.instrings(res)}')

    print(f'{mod.func(2,8,10,13)}')
    print(f'{mod.pas(input())}')
except NameError:
    print(f'Ошибка выполнения')
