class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._cache = dict()

    def print_cache(self) -> None:
        print(self._cache)

    @cache.setter               # TODO не могу понять почему он не видит имя "cache".
                                #  Скорее всего не верно объявляю в __init__
    def cache(self, key: str, value: str) -> None:
        self._cache[key] = value

    @property
    def get(self, key):
        return self._cache[key]



# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4