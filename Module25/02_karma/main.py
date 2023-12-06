import random


class Monk:
    def __init__(self, karma):
        self.karma = karma


    def one_day(self):
        daily_karma = random.randint(1, 7)
        return daily_karma


class KillError(BaseException):
    print('Не убей')


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
        for unluck in range(random.randint(1, 10)):
            if unluck == 1:
                error_name = random.choice(['KillError', 'DrunkError', 'CarCrashError',
                                             'GluttonyError', 'DepressionError'])
                raise error_name #TODO почемуто вызывает все ошибки сразу, а компилятор ругается, \
                                 # raise error_name
                                 # TypeError: exceptions must derive from BaseException
                                 # Ошибки должны происходить от BaseException
                                 # а как это правильно в классе прописать?
    except KillError:
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