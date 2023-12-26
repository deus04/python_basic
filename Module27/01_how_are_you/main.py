

def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        question = input('Как дела? ')
        print('Ладна, проехали')
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@my_decorator
def test():
    print('<Тут чтото происходит...>')


test()