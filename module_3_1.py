#Цель: применить на практике начальные знания о пространстве имён и оператор global. Закрепить навыки из предыдущих модулей.
calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(name):
    count_calls()
    string = len(name), name.upper(), name.lower()
    return string
def is_contains(first_, second_):
    count_calls()
    first1 = first_
    first= first1.lower()
    second3 = second_
    second2 = str(second3)
    second = second2.lower()
    if first in second:
        return True
    else:
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

