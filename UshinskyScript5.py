try:
    import numpy as np
except ModuleNotFoundError:
    print(f'Модуль с таким именем не найден')
try:
    print(f'{np.random.sample((3, 3))}')
except NameError:
    print(f'Ошибка выполнения')
