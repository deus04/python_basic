import math


class MyMath:
    # TODO забыли указать декоратор @classmethod для каждого метода
    def circle_len(radius):
        L = 2 * radius * math.pi  # TODO имена переменных пишутся исключительно строчными буквам (см. РЕР 8)
        return L

    # TODO Аналогично предыдущему для всего остального кода класса
    def circle_sq(radius):
        S = math.pi * radius**2
        return S

    def volume_cube(side):
        V = side**3
        return V

    def surface_area_sphere(radius):
        S = 4 * math.pi * radius**2
        return S


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
res_3 = MyMath.volume_cube(side=5)
print(res_3)
res_4 = MyMath.surface_area_sphere(radius=10)
print(res_4)