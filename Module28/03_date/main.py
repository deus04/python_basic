class Date:
    @classmethod
    def from_string(cls, string):
        splited_str = string.split('-')
        date = 'День: {}        Месяц: {}       Год: {}'\
            .format(splited_str[0], splited_str[1], splited_str[2])
        return date

    @classmethod
    def is_date_valid(cls, string):
        splited_str = string.split('-')
        if (0 < int(splited_str[0]) <= 31) and (0 < int(splited_str[1]) <= 12) and (0 < int(splited_str[2])):
            # просто верните результат сравнения
            #  почему? в задании результат True or False
            # TODO Потому что именно эти значения и являются результатом сравнения!
            #  Тема эта называется "булева логика", рекомендую к освежению в памяти
            #  https://dzen.ru/a/Y_2lH1ADETu2ccVx
            #  https://timeweb.cloud/tutorials/python/logicheskie-vyrazheniya-i-operatory-v-python-3?ysclid=lryij86pwl158760276
            return True
        return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
