#Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
average_grades = {}
for i in range(len(grades)):
    average_grade = sum(grades[i]) / len(grades[i])

    average_grades[students_list[i]] = average_grade
print(average_grades)