class SquarerIter:

    def __init__(self, stop_number):
        self.stop_number = stop_number
        self.start_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_number < self.stop_number:
            self.start_number += 1
            return self.start_number ** 2
        else:
            raise StopIteration


def squarer_gen(stop_number):
    start_number = 0
    for _ in range(stop_number):
        start_number += 1
        yield start_number ** 2


number = 10

print('Iterator: ')
my_squarer_iter = SquarerIter(number)
for i_num in my_squarer_iter:
    print(i_num, end=' ')

print('\nGenerator: ')
my_squarer_gen = squarer_gen(number)
for i_num in my_squarer_gen:
    print(i_num, end=' ')

print('\nExpression: ')
my_generator_expression = (i_num ** 2 for i_num in range(1, number + 1))
for i_num in my_generator_expression:
    print(i_num, end=' ')
