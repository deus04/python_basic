class Date:
    @classmethod
    def from_string(cls, string):
        splited_str = string.split('-')
        date = 'День: {}\tМесяц: {}\tГод: {}'\
            .format(splited_str[0], splited_str[1], splited_str[2])
        return date

    @classmethod
    def is_date_valid(cls, string):
        splited_str = string.split('-')
        return (0 < int(splited_str[0]) <= 31) and (0 < int(splited_str[1]) <= 12) and (0 < int(splited_str[2]))


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
