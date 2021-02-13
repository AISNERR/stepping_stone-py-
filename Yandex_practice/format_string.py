weather = 'облачно'
print(f'На улице сейчас {weather}.')

# Сравните с
print('На улице сейчас ' + weather + '.')
# или
print('На улице сейчас', weather, '.')
# в таком коде не убрать пробел перед точкой
#форматирование строк - есть возможность вычислений операций уже в скобках
one_hundred = 100
five_hundred = 500
print(f'{one_hundred} + {five_hundred} = {one_hundred + five_hundred}')

one_hundred = 'сто'
five_hundred = 'пятьсот'
print(f'{one_hundred} + {five_hundred} = {one_hundred + five_hundred}')