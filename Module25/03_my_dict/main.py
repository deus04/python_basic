
class MyDict(dict):

    def get(self, key):
        result = 0
        for i_key, i_value in self.items():  # TODO просто получите нужное с помощью метода get или по имени ключа
                                             #  (предварительно надо проверить наличие ключа в словаре оператором in)
            if key == i_key:
                result = i_value
        return result


my_dict = MyDict()

my_dict['one'] = 1
my_dict['three'] = 3
my_dict['four'] = 4
test = my_dict.get('four')
print(test)
print(my_dict.get('five'))


# new_dict = dict()
# new_dict['two'] = 2
# b = new_dict.get('3', 0)
# print(b)
