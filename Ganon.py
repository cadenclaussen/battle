from Mob import *
import random

class Ganon(Mob):

    def __init__(self, name):
        super().__init__(name, random.randint(23000, 25000), 90)
        self.attacks["spear throw"] = self.spear_throw
        self.attacks["laser"] = self.laser_attack

    def spear_throw(self, target):
        super().attack("spear throw", target, random.randint(750, 1000))

    def laser_attack(self, target):
        super().attack("laser", target, random.randint(1000, 1250))
