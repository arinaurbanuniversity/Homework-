def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
'''
#1.Функция с параметрами по умолчанию
print_params(1, '2')
print_params(35)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

#2.Распаковка параметров
values_list = [1, 'два', True]
values_dict = { 'a': 1, 'b': 2, 'c': 3 }
print_params(*values_list)
print_params(**values_dict)'''

#3.Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
