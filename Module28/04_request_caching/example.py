class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__cache = {}
        self.order = []

    @property
    def cache(self):
        key_for_del = self.order[0]
        result = key_for_del, self.__cache[key_for_del]
        return result

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.__cache:
            # Перемещаем ключ в конец списка order
            self.order.remove(key)
            self.order.append(key)
        else:
            # Добавляем новый ключ в кэш и список order
            self.__cache[key] = value
            self.order.append(key)

            # Если превышен лимит capacity, удаляем самый старый элемент
            if len(self.order) > self.capacity:
                oldest_key, oldest_value = self.cache
                self.order.pop(0)
                del self.__cache[oldest_key]

    def get(self, key):
        if key in self.__cache:
            # Перемещаем ключ в конец списка order
            self.order.remove(key)
            self.order.append(key)
            return self.__cache[key]
        else:
            return None

    def print_cache(self):
        print("LRU Cache:")
        for key in self.order:
            print(key, ":", self.__cache[key])


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
