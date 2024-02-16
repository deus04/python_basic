from typing import List
from functools import reduce


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

round_floats = list(map(lambda i_float: round(i_float**3, 3), floats))
print(round_floats)

long_names = list(filter(lambda i_name: len(i_name) >= 5, names))
print(long_names)

product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)
