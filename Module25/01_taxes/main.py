class Property:
    tax = 1
    #  правильно ли будет определить переменную tax = 1, при условии что мы ее меняем в потомках?
    #  как будто было бы правильно ее прописать в родителе
    # TODO Вполне возможно, переопределение части атрибутов и методов это в правилах ООП
    def __init__(self, worth):
        self.worth = worth
    pass  # TODO эта строка лишняя, pass ставят вместо реализации метода/функции/класса, если она не нужна или отложена "на потом"

    def tax_calculation(self):
        total_price = self.worth * self.tax
        return total_price


class Apartment(Property):
    tax = 1/1000
    pass  # TODO Аналогично предыдущему


class Car(Property):
    tax = 1 / 200
    pass


class CountryHouse(Property):
    tax = 1 / 500
    pass


money = int(input('Сколько денег у вас есть?\n'))

apartment = Apartment(int(input('Сколько стоит квартира?\n')))

car = Car(int(input('Сколько стоит машина?\n')))

country_house = CountryHouse(int(input('Сколько стоит дача?\n')))

tax_apartment = apartment.tax_calculation()
print('Налог на квартиру:', tax_apartment)
tax_car = car.tax_calculation()
print('Налог на машину:', tax_car)
tax_country_house = country_house.tax_calculation()
print('Налог на дачу:', tax_country_house)


total_tax = tax_car + tax_apartment + tax_country_house
remainder = money - total_tax
print('\nНужно заплатить {}'.format(total_tax))
if remainder > 0:
    print('Все хорошо, у Вас останется еще {} '.format(remainder))
else:
    print('К сожалению у Вас недостаточно средств')
