numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    counter = 0
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            counter = counter + 1
    if counter > 0:
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])
print('Простые числа:' + str(primes))
print('Не простые числа:' + str(not_primes))
