#Цель: закрепить навык решения задач при помощи цикла for, применив знания об основных типах данных.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
primes = []
not_primes = []
numbers.remove(1)
for number in numbers:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print("Primes:", primes)
print("Not Primes:", not_primes)

