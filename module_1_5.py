#Цель: Написать программу на языке Python, используя Pycharm, для работы с неизменяемыми и изменяемыми объектами.
immutable_var = ("Apple", "Banana", "Orange", "Pear", "Cherry", "Kiwi")
print("Кортежи:", immutable_var)
#immutable_var[0] = "Pineapple"  - Выше перечисленные элементы — это все кортежи. Кортеж — это коллекция элементов, обладающая такой особенностью, как неизменяемость. Из-за этого мы не можем изменить значение в переменной кортежа.
mutable_list = ["Lion", "Elephant", "Giraffe", "Dolphin", "Kangaroo"]
print("Список:", mutable_list)
mutable_list[0] = "Penguin"
print("Изменение элемента в списке:", mutable_list)


