from collections import Counter


def count_unique_characters(string):
    lower_string = string.lower()
    return sum(list(filter(lambda i_value: i_value == 1, Counter(lower_string).values())))



# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
