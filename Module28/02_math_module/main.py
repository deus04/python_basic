import math


class MyMath:
    @classmethod
    def circle_len(cls, radius):
        l = 2 * radius * math.pi
        return l

    @classmethod
    def circle_sq(cls, radius):
        s = math.pi * radius**2
        return s

    @classmethod
    def volume_cube(cls, side):
        v = side**3
        return v

    @classmethod
    def surface_area_sphere(cls, radius):
        s = 4 * math.pi * radius**2
        return s


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
res_3 = MyMath.volume_cube(side=5)
print(res_3)
res_4 = MyMath.surface_area_sphere(radius=10)
print(res_4)