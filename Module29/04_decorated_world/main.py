
def decorator_with_args_for_any_decorator(decorator):
    def wrapper_decorator(*decorator_args, **decorator_kwargs):
        def actual_decorator(func):
            def wrapper_function(*args, **kwargs):
                print("Переданные арги и кварги в декоратор: {} {}".format(decorator_args, decorator_kwargs))
                return func(*args, **kwargs)
            return decorator(wrapper_function, *decorator_args, **decorator_kwargs)
        return actual_decorator
    return wrapper_decorator



@decorator_with_args_for_any_decorator
def decorated_decorator(func, *args, **kwargs):
    def wrapper_function(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper_function


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)