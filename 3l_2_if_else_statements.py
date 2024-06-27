num1 = 4
num2 = 5

if num1 > num2:
    print(f'{num1=} > {num2=}')
elif num1 < num2:
    print(f'{num1=} < {num2=}')
else:
    print("equal")

card_number = '4400 .... .... ....'
if card_number.startswith('4444'):
    print(f'Card is valid')
else:
    print(f'Card is invalid')

names = 'John, JJ, Mike, Tom'
if 'John' in names:
    print(f'hello john')
else:
    print('where is john?')

# zero-values
int_number = 0 # False

if int_number:
    print(True)
else:
    print(False)