class Water:
    name = 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return storm
        elif isinstance(other, Fire):
            return steam
        elif isinstance(other, Earth):
            return mud
        else:
            return None

    def __str__(self):
        return self.name


class Air:
    name = 'Air'

    def __add__(self, other):
        if isinstance(other, Water):
            return storm
        elif isinstance(other, Fire):
            return lightning
        elif isinstance(other, Earth):
            return dust
        else:
            return None

    def __str__(self):
        return self.name


class Fire:
    name = 'Fire'

    def __add__(self, other):
        if isinstance(other, Fire):
            return steam
        elif isinstance(other, Air):
            return lightning
        if isinstance(other, Earth):
            return lava
        else:
            return None

    def __str__(self):
        return self.name


class Earth:
    name = 'Earth'

    def __add__(self, other):
        if isinstance(other, Water):
            return mud
        elif isinstance(other, Air):
            return dust
        if isinstance(other, Fire):
            return lava
        else:
            return None

    def __str__(self):
        return self.name


class Storm:
    name = 'Storm'

    def __add__(self, other):
        return None

    def __str__(self):
        return self.name


class Steam:
    name = 'Steam'

    def __add__(self, other):
        return None

    def __str__(self):
        return self.name


class Mud:
    name = 'Mud'

    def __add__(self, other):
        return None

    def __str__(self):
        return self.name


class Lightning:
    name = 'Lightning'

    def __add__(self, other):
        return None

    def __str__(self):
        return self.name


class Dust:
    name = 'Dust'

    def __add__(self, other):
        return None

    def __str__(self):
        return self.name


class Lava:
    name = 'Lava'

    def __add__(self, other):
        return None

    def __str__(self):
        return self.name


water = Water()
air = Air()
fire = Fire()
earth = Earth()

dust = Dust()
lava = Lava()
storm = Storm()
steam = Steam()
mud = Mud()
lightning = Lightning()

print(water + air)
print(water + fire)
print(water + earth)
print(air + fire)
print(air + earth)
print(fire + earth)
print(water + dust)
print(dust + lava)



