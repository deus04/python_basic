number = int(input("Введите число:"))
odd_numbers = []

for i in range(number + 1):  # TODO используйте параметр ШАГ, чтобы упростить код за счёт избавления от условного оператора
    if i % 2 == 1:
        odd_numbers.append(i)

print("Список из нечётных чисел от одного до", number, ":", odd_numbers)
