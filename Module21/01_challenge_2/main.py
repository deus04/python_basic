def deep_count(num):
    if num <= 1:
        print(num)
    else:
        deep_count(num - 1)
        print(num)


num = int(input("Введите num: "))
deep_count(num)
