class Water:
    name = 'Water'

    def __add__(self, other):
        if other.name == 'Air':
            return Storm.name
        elif other.name == 'Fire':
            return Steam.name
        elif other.name == 'Earth':
            return Mud.name
        else:
            return None


class Air:
    name = 'Air'

    def __add__(self, other):
        if other.name == 'Water':
            return Storm.name
        elif other.name == 'Fire':
            return Lightning.name
        elif other.name == 'Earth':
            return Dust.name
        else:
            return None


class Fire:
    name = 'Fire'

    def __add__(self, other):
        if other.name == 'Fire':
            return Steam.name
        elif other.name == 'Air':
            return Lightning.name
        if other.name == 'Earth':
            return Lava.name
        else:
            return None


class Earth:
    name = 'Earth'

    def __add__(self, other):
        if other.name == 'Water':
            return Mud.name
        elif other.name == 'Air':
            return Dust.name
        if other.name == 'Fire':
            return Lava.name
        else:
            return None


class Storm:
    name = 'Storm'

    def __add__(self, other):
        return None


class Steam:
    name = 'Steam'

    def __add__(self, other):
        return None


class Mud:
    name = 'Mud'

    def __add__(self, other):
        return None


class Lightning:
    name = 'Lightning'

    def __add__(self, other):
        return None


class Dust:
    name = 'Dust'

    def __add__(self, other):
        return None


class Lava:
    name = 'Lava'

    def __add__(self, other):
        return None


water = Water()
air = Air()
fire = Fire()
earth = Earth()
dust = Dust()
lava = Lava()

print(water + air)
print(water + fire)
print(water + earth)
print(air + fire)
print(air + earth)
print(fire + earth)
print(water + dust)
print(dust + lava)



