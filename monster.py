# monster.py
import random
# 4. Move your class definitions into specific python files hero.py and monster.py
# 2. Make a Monster class


class Monster:

    # 2b Add m_combat_strength and m_health_points as properties of the class
    m_combat_strength = 0
    m_health_points = 0

    # 2c Create an init method (constructor) that rolls the dice for combat strength and health points.
    def __init__(self):
        self.m_combat_strength = random.randint(1, 20)
        self.m_health_points = random.randint(50, 100)

    # 3 Convert to using the complex getters and setters for ALL of your classes
    # Monster Combat Strength Property
    @property
    def m_combat_strength(self):
        return self.__m_combat_strength

    @m_combat_strength.setter
    def m_combat_strength(self, value):
        print('m_combat_strength Setted to {}'.format(value))
        self.__m_combat_strength = value

    @m_combat_strength.deleter
    def m_combat_strength(self):
        print("m_combat_strength is deleted")
        del self.__m_combat_strength

    # Monster Health Points Property
    @property
    def m_health_points(self):
        return self.__m_health_points

    @m_health_points.setter
    def m_health_points(self, value):
        print('m_health_points Setted to {}'.format(value))
        self.__m_health_points = value

    @m_health_points.deleter
    def m_health_points(self):
        print("m_health_points is deleted")
        del self.__m_health_points

    # 2a Add method monster_attacks() inside the class.
    def monster_attacks():
        return 0

    # 2d Create a del method (destructor)
    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
