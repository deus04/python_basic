import random


class Monk:
    def __init__(self, karma):
        self.karma = karma


    def one_day(self):  # TODO Определение метода должно отделяться от остального кода класса одной пустой строкой
        daily_karma = random.randint(1, 7)
        # TODO выбрасывать исключения надо тоже тут (с заданной в условии вероятностью), а ловить и обрабатывать их
        #  надо в основном коде программы
        return daily_karma


class KillError(BaseException):
    # TODO базовый класс всех простых исключений это Exception, а BaseException это "внутренности"
    #  реализации и обычно не используется
    print('Не убей')  # TODO нет никакого смысла выводить это в консоль при чтении кода интерпретатором (а именно это
                      #  происходит непосредственно перед запуском кода на исполнение).
                      #  Тут как раз уместно использовать pass


class DrunkError(BaseException):
    print('Не пей')


class CarCrashError(BaseException):
    print('Ехай давай')


class GluttonyError(BaseException):
    print('Не хавай')


class DepressionError(BaseException):
    print('Не грусти')


monk = Monk(0)
with open('karma.log', 'w') as file:
    try:
        monk.karma += monk.one_day()
        for unluck in range(random.randint(1, 10)):  # TODO весь код выбрасывания исключений перенесите в one_day
            if unluck == 1:
                error_name = random.choice(['KillError', 'DrunkError', 'CarCrashError',
                                             'GluttonyError', 'DepressionError'])
                raise error_name # почемуто вызывает все ошибки сразу, а компилятор ругается, \
                                 # raise error_name
                                 # TypeError: exceptions must derive from BaseException
                                 # Ошибки должны происходить от BaseException
                                 # а как это правильно в классе прописать?
            # TODO выбрасывать можно только классы исключений, а не строки. В списке выше вместо строк имён
            #  классов используйте объекты исключений с поясняющими сообщениями. Ловить исключения и логгировать их надо
            #  в основном коде программы (вспомните задачу 3 из модуля 23) - сделайте это одной веткой except
            #  Доп. материал: https://pythonstart.ru/list/polzovatelskie-isklyucheniya-python?ysclid=lplh9zxilt629346438
    except KillError:
        # TODO тут надо логгировать произошедшие исключения
        pass
    except DrunkError:
        pass
    except CarCrashError:
        pass
    except GluttonyError:
        pass
    except DepressionError:
        pass
    else:
        print("Нет ошибок")



'''
По итогу у вас может быть примерно такая структура программы:

открываем файл

цикл по набору кармы

   try

      карма += one_day()

   except(ы) с указанием классов исключений, которые нужно поймать

      добавляем запись в файл

закрываем файл
'''