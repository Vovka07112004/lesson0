#Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
def generate_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += f"{i}{j}"
    return result
for n in range(3, 21):
    password = generate_password(n)
    print(f"{n} - {password}")
