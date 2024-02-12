app = dict()


def callback(path):
    def decorator(func):
        app[path] = func

        def wrapper(*args, **kwargs):
            if path in app:
                result = func(*args, **kwargs)
                return result
        return wrapper
    return decorator


@callback('//')
def route():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
