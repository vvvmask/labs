name = 'Dias'
age = 22
print('name is %s and age is %s' % (name, age))

# better way
print('name is {name} and age is {age}'.format(name=name,age=age))

#the best way
print(f'name is {name} and age is {age}')

number = 1
print(f'the number is {number}')
print(f'the number is {number:013}')

for i in range(11):
    print(f'the number is {i:2}')

float_number = 33.33333
print(f'{float_number:.2f}')

percent = 0.1565
print(f'{percent:.1%}')

person = 'dias'
print(f'{person:>10}')
print(f'{person:^10}')
print(f'{person:<10}')
print(f'{person:$^6}')

ten_billion_dollars = 1000000000
print(f'{ten_billion_dollars:,}$')

name = 'Dias'
surname = 'Galiyev'
print(f'name={name}, surname ={surname}')
print(f'{name=}, {surname=}')

def index(a):
    return print(f'{a=}')
index("dias galiyev")
