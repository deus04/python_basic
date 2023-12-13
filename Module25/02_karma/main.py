import random


class Monk:
    def __init__(self, karma):
        self.karma = karma

    def one_day(self):
        daily_karma = random.randint(1, 7)
        if random.randint(1, 10) == 1:
            error_name = random.choice([KillError('Не убей'), DrunkError('Не пей'), CarCrashError('Ехай давай'),
                                        GluttonyError('Не хавай'), DepressionError('Не грусти')])
            raise error_name
        return daily_karma


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


monk = Monk(0)
with open('karma.log', 'w', encoding='utf-8') as karma_log:
    while monk.karma < 500:
        try:
            monk.karma += monk.one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            error_message = f'Уровень кармы - {monk.karma} - {exc.__class__.__name__} - {exc}\n'
            karma_log.write(error_message)

