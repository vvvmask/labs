#stack - область памяти, которая используется для хранения временных данных
#heap - область памяти, предназначенная для динамического распределения данных

a = 5
b = 4
print(property(id(a)))
print(property(id(b)))

c = 5
d = c
print(property(id(c), id(d)))