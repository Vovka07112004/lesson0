#Цель: применить навыки создания цикла while, а так же применения операторов break и continue.
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    current_number = my_list[index]
    if current_number > 0:
        print(current_number)
    if current_number < 0:
        break
    index += 1











