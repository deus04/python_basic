def callback(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if path:
                result = func(*args, **kwargs)
                return result
        return wrapper
    return decorator


@callback('//')
def route():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


#route = app.get('//')    TODO не понял куда эта строчка

if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')