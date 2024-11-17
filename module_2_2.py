#Цель: применить навыки создания условных конструкций и знания операторов if, else, elif / and, or, not.
print("Напишите три трехзначных числа!")
first =int(input("Введите первое трехзначное число: "))
second =int(input("Введите второе трехзначное число: "))
third  =int(input("Ведите третье трехзначное число: "))
if first == second == third:
    print(3) # Все числа равны
elif first == second or first == third or second == third:
    print(2)# Хотя бы два числа равны
else:
    print(0)# Равных чисел нет
