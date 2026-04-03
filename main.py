def powers_of_three(n):
    for i in range(n):
        yield 3 ** i

count = int(input("Скільки ступенів числа 3 вивести? "))

for value in powers_of_three(count):
    print(value)