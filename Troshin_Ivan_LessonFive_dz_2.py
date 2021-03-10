n = input('Введите число "n" :')
nums_gen = (num for num in range(1, int(n) + 1) if num % 2 == 1)
print(*nums_gen)
