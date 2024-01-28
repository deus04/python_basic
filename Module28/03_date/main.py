class Date:
    def from_string(string):
        splited_str = string.split('-')
        date = 'День: {}        Месяц: {}       Год: {}'\
            .format(splited_str[0], splited_str[1], splited_str[2])
        return date

    def is_date_valid(string):
        splited_str = string.split('-')
        if (0 < int(splited_str[0]) <= 31) and (0 < int(splited_str[1]) <= 12) and (0 < int(splited_str[2])):
            return True
        else:
            return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))