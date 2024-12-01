#Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(list(students))
average_grades = {}
for i in range(len(sorted_students)):
    student_name = sorted_students[i]
    student_grades = grades[i]
    average_grade = sum(student_grades) / len(student_grades)
    average_grades[student_name] = average_grade
print(average_grades)