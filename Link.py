from Mob import *
import random

class Link(Mob):
    def __init__(self, name):
        super().__init__(name, 5000, 95)
        self.attacks["spin"] = self.spin_attack
        self.attacks["slam"] = self.slam_attack
        self.attacks["combo"] = self.combo_attack

    def spin_attack(self, target):
        super().attack("spin", target, random.randint(500, 750))

    def slam_attack(self, target):
        super().attack("slam", target, random.randint(600, 850))

    def combo_attack(self, target):
        super().attack("combo", target, random.randint(500, 850))
