def check_permission(user_permissions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                if user_permissions == 'admin':
                    result = func(*args, **kwargs)
                    return result
                else:
                    raise PermissionError
            except PermissionError:
                print('У пользователя недостаточно прав, чтобы выполнить функцию', func.__name__)
        return wrapper
    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

