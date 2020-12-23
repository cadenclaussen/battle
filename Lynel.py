from Mob import *
import random



class Lynel(Mob):

    def __init__(self, name, health, heal_multiplier):
        super().__init__(name, health, heal_multiplier)
        self.attacks["spear charge"] = self.spear_charge
        self.attacks["fire slam"] = self.fire_slam
        self.attacks["breath fire"] = self.spear_charge
        self.attacks["stamp"] = self.fire_slam



class GoldLynel(Lynel):

    def __init__(self, name):
        super().__init__(name, random.randint(4000, 5000), 70)

    def spear_charge(self, target):
        super().attack("spear charge", target, random.randint(250, 750))

    def fire_slam(self, target):
        super().attack("fire slam", target, random.randint(750, 1000))

    def breath_fire(self, target):
        super().attack("breath fire", target, random.randint(100, 250))

    def stamp(self, target):
        super().attack("stamp", target, random.randint(500, 750))



class SilverLynel(Lynel):

    def __init__(self, name):
        super().__init__(name, random.randint(2000, 3000), 60)

    def spear_charge(self, target):
        super().attack("spear charge", target, random.randint(150, 650))

    def fire_slam(self, target):
        super().attack("fire slam", target, random.randint(650, 900))

    def breath_fire(self, target):
        super().attack("breath fire", target, random.randint(0, 150))

    def stamp(self, target):
        super().attack("stamp", target, random.randint(400, 650))
