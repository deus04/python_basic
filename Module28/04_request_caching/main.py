class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.__cache = dict()  # по классике этот атрибут делаем приватным, то есть с префиксом из двойного подчеркивания
        self.cache_list = list()

    def print_cache(self) -> None:
        print(self.__cache)

    @property
    def cache(self, key: str) -> None:
        return self.__cache[key]    #  сеттер заработал, но что тогда в проперти нужно возвращать?
                                    # TODO Свойство (не стоит писать транслитом) обычно возвращает значение атрибута,
                                    #  причем свойство не должно иметь параметров. В нашем случае надо возвращать самый
                                    #  "старый" элемент, то есть помещённый в кэш раньше остальных

    @cache.setter               #  не могу понять почему он не видит имя "cache".
                                #  Скорее всего не верно объявляю в __init__
                                # определите свойство до сеттера и всё получится
    def cache(self, key_value) -> None:  # на самом деле нам нужен метод который принимает один параметр в виде кортежа из ключа и значения
        key, value = key_value
        if key in self.cache_list:
            self.cache_list.remove(key)
        self.cache_list.append(key)
        self.__cache[key] = value
        if len(self.__cache) > self.capacity:
            oldest_key = self.cache_list[0]
            self.cache_list.remove(oldest_key)
            self.__cache.pop(oldest_key)  #  нужно придумать как удалить самый старый
                                          #  возможно не самый эффективынй способ нахождения нужного ключа
      # TODO Однако получился достаточно лаконичный алгоритм. Конечно вариантов реализации может быть
      #  много, зависит от фантазии. Предлагаю к ознакомлению вариант решения в файле example.py Возможно он натолкнёт
      #  вас на другое, более оптимальное решение

    def get(self, key: str) -> None:
        return self.__cache[key]




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