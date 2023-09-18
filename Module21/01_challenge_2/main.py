def deep_count(num):
    if num <= 1:
        print(num)  # TODO эта строка может выполняться безусловно, вынесите её из if
    else:
        deep_count(num - 1)
        print(num)


num = int(input("Введите num: "))
deep_count(num)
