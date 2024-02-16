from collections import Counter


def can_be_poly(string):
    return len(string) % 2 == sum(map(lambda i_elem: i_elem % 2, Counter(string).values()))


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))