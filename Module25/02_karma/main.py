import random


class Monk:
    def __init__(self, karma):
        self.karma = karma

    def one_day(self):
        daily_karma = random.randint(1, 7)
        if random.randint(1, 10) == 1:
            error_name = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
            raise error_name
        return daily_karma


class KillError(Exception):
    advice = 'Не убей'
    # TODO более общепринятым (стандартным) способом указания поясняющего сообщения, является использование механизма
    #  уже реализованного в Exception - передавать его объекту класса исключения при его создании. В данном случае
    #  сообщения можно указать в списке выше:
    #  error_name = random.choice([KillError('Не пей'), ....])
    #  тогда при логгировании поясняющего сообщения не пришлось бы указывать атрибут advice


class DrunkError(Exception):
    advice = 'Не пей'


class CarCrashError(Exception):
    advice = 'Ехай давай'


class GluttonyError(Exception):
    advice = 'Не хавай'


class DepressionError(Exception):
    advice = 'Не грусти'


monk = Monk(0)
with open('karma.log', 'w', encoding='utf-8') as karma_log:
    while monk.karma < 500:
        try:
            monk.karma += monk.one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            error_message = f'Уровень кармы - {monk.karma} - {exc.__class__.__name__} - {exc.advice}\n'
            karma_log.write(error_message)

