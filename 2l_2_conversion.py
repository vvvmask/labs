str_integer = '123'
int_number = int(str_integer)
print(int_number, type(int_number))

str_float = '123.235'
float_number = float(str_float)
print(float_number, type(float_number))

qs = '''
    SELECT *
    FROM orders
    WHERE order = ''
'''

str_bool_true = 'True'
str_bool_false = 'False'
print(bool(str_bool_true), bool(str_bool_false))

# zero value
# default value
zero_integer = 0
zero_float = 0.0
empty_string = ''
arr = []
e_dict = {}
e_set = set()
print(bool(zero_integer), bool(zero_float))
