#Цель: Написать программу на языке Python, используя Pycharm, для работы со словарями и множествами.
#Работа со словарями
my_dict = {"Alexander": 1799, "Anna": 1889, "Fyodor": 1821, "Leo" : 1828}
print("Название:", my_dict)
print("Существующее значение:", my_dict["Alexander"])
print("Несуществующее значение:", my_dict.get("Anton"))
my_dict.update({"Mikhail": 1891, "Vasily": 1905})
a = my_dict.pop("Anna")
print("Удалено значение:", a)
print("Измененный словарь:", my_dict)
# Работа с множествами
my_set = {1, 2, 3, 8, 2, 76.55, 7, True, False, True, "UrBan", "How are you?"}
print("Набор:", my_set)
my_set.update({45, "Hello"})
print("Добавление переменных:", my_set)
my_set.discard(2)
print("Измененный набор:", my_set)

