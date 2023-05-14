number = int(input("Введите число:"))
odd_numbers = []

for i in range(number + 1):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Список из нечётных чисел от одного до", number, ":", odd_numbers)
