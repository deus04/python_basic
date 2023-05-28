alphabet = 'abcdefg'

copy_alphabet = alphabet[:]
print('1:', copy_alphabet)

alphabet_reverse = alphabet[::-1]
print('2:', alphabet_reverse)

every_second = alphabet[::2]
print('3:', every_second)

every_second_without_first = alphabet[1::2]
print('4:', every_second_without_first)

all_up_to_second = alphabet[:1:]
print('5:', all_up_to_second)

from_end_to_penultimate = alphabet[:-2:-1]
print('6:', from_end_to_penultimate)

from_3_without_4 = alphabet[3:4]
print('7:', from_3_without_4)

last_three = alphabet[-3::]
print('8:', last_three)

from_3_to_4 = alphabet[3:5]
print('9:', from_3_to_4)

from_4_to_3 = alphabet[4:2:-1]
print('10:', from_4_to_3)


