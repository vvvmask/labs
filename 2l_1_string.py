full_name = 'Dias Galiyev'

print(f'strip(): {full_name.strip()}') # срезает whitespace
print(f'title(): {full_name.title()}') # Символ каждого слова в вверхний регистр
print(f'capitalizer(): {full_name.capitalize()}') # Первый символ в вверхний регистр, остальные в нижний
print(f'lower(): {full_name.lower()}') # В нижний регистр
print(f'upper(): {full_name.upper()}') # В верхний регистр
print(f'count(): {full_name.count("a")}') # Считает количество символов в строке
print(f'startswith(): {full_name.startswith("D")}') # начинается ли строка с указанного символа
print(f'endswith(): {full_name.endswith("v")}') # заканчивается ли строка указанным символом

print(f'isdigit(): {"123".isdigit()}') # если строка цифровая, то возвращает True
print(f'islower(): {full_name.islower()}') # Возвращает true если символы в нижнем регистре
print(f'isupper(): {"123".isupper()}') # Возвращает true если строка в вверхнем регистре
print(f'isspace(): {full_name.isspace()}') # Если строка состоит из пробелов

print(f'find(): {full_name.find("w")}') # Вернет порядковый номер массива при поиске
print(f'index(): {full_name.index("v")}') # Отличается от find, если не находит, то выдает ошибку
print('a' in full_name) # Возвращает true если есть 'a' в строке


car = 'BMW'
print(f'car: {car}')
print(car[0], car[1], car[2], sep=',')

car_copy = car[:]
print(f'car_copy: {car_copy}')

reverse_car = car[::-1]
print(f'reverse_car: {reverse_car}')

issued_text_order = 'Заказ с номером {order_number} был выписан'
print(issued_text_order.format(order_number=1))
print(issued_text_order.format(order_number='2d'))
print(issued_text_order.format(order_number=1.235))

full_name = (
    'asdasd'
    'fafasf'
)
print(f'full_name: {full_name}')
