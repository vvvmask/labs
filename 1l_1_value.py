# Первый урок из плейлиста по Python

# Типы переменных
integer_num = 1
float_num = 1.5
complex_num =  1 + 2j

print(f'integer_number: {integer_num}, type: {type(integer_num)}')
print(f'float_number: {float_num}, type: {type(float_num)}')
print(f'complex_number: {complex_num}, type: {type(complex_num)}')

# operations + , - , * , /
wallet = 1 + 214
print(f'wallet: {wallet}, type: {type(wallet)}')

wallet = 2 * 10 / 3
print(f'wallet: {wallet}, type: {type(wallet)}')

wallet = 5 // 2 # Деление без остатка, оставляет только целую часть
print(f'wallet: {wallet}, type: {type(wallet)}')

wallet = 5 % 2 # Деление с остатком, оставляет остаточную часть от деления
print(f'wallet: {wallet}, type: {type(wallet)}')

wallet = 4 ** 2 # Возведение в степень
print(f'wallet: {wallet}, type: {type(wallet)}')
