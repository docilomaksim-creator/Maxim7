try:
    number = input("Введіть число: ")

    number = int(number)

    print("Ви ввели ціле число:", number)

except ValueError:
    print("Помилка! Введені дані не можна конвертувати в число.")