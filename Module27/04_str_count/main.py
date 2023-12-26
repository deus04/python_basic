
def counter(func):

    def wrapped_func(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapped_func.count += 1
        return result

    wrapped_func.count = 0
    return wrapped_func


@counter
def test():
    print('<Тут чтото происходит...>')


@counter
def test_2():
    print('<Тут чтото происходит...>')


for _ in range(5):
    test()

for _ in range(2):
    test_2()

print(test.count)
print(test_2.count)


