# hero.py
import random
# 4. Move your class definitions into specific python files hero.py and monster.py
# 1. Make a Hero class


class Hero:
    # 1b Add combat_strength and health_points as properties of the class
    __combat_strength = 0
    __health_points = 0

    # 1c Create an init method (constructor) that rolls the dice for combat strength and health points.
    def __init__(self):
        self.__combat_strength = random.randint(1, 20)
        self.__health_points = random.randint(50, 100)

    # 3 Convert to using the complex getters and setters for ALL of your classes
    # Combat Strength Property
    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        print('combat_strength Setted to {}'.format(value))
        self.__combat_strength = value

    @combat_strength.deleter
    def combat_strength(self):
        print("combat_strength is deleted")
        del self.__combat_strength

    # Health Points Property
    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        print('health_points Setted to {}'.format(value))
        self.__health_points = value

    @health_points.deleter
    def health_points(self):
        print("health_points is deleted")
        del self.__health_points

    # 1a Add method hero_attacks() inside the class.

    def hero_attacks():
        return 0

    # 1d Create a del method (destructor)
    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
