#Цель задания: Освоить создание функций с параметрами по умолчанию и практику вызова этих функций с различным количеством аргументов.
def print_params(a=1, b='строка', c=True):
    print(f'a: {a}, b: {b}, c: {c}')
# 1. Вызовы функции с разным количеством аргументов
print_params()
print_params(10)
print_params(10, 'новая строка')
print_params(10, 'новая строка', False)
print_params(b=25)
print_params(c=[1, 2, 3])
# 2. Распаковка параметров
values_list = [42, 'hello', False]
values_dict = {'a': 99, 'b': 'world', 'c': True}
print("Вызов с распаковкой списка:")
print_params(*values_list)
print("Вызов с распаковкой словаря:")
print_params(**values_dict)
# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print("Вызов с распаковкой и отдельным параметром:")
print_params(*values_list_2, 42)
