numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    is_prime = True  # Предполагаем, что число простое
    if number <= 1:  # 1 не является ни простым, ни составным
        continue
    for i in range(2, number):  # Проверяем делители от 2 до числа (не включая число)
        if number % i == 0:
            is_prime = False  # Число не простое
            break  # Прекращаем проверку, как только нашли делитель

    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")


