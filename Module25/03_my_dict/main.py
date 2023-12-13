
class MyDict(dict):

    def get(self, key):
        return super().get(key, 0)


my_dict = MyDict()

my_dict['one'] = 1
my_dict['three'] = 3
my_dict['four'] = 4
print(my_dict.get('four'))
print(my_dict.get('five'))

