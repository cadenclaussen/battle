from Mob import *
import random



class Guardian(Mob):

    def __init__(self, name):
        super().__init__(name, random.randint(9000, 10000), 50)
        self.attacks["swirl attack"] = self.swirl_attack
        self.attacks["jump attack"] = self.jump_attack

    def swirl_attack(self, target):
        super().attack("swirl attack", target, random.randint(100, 400))

    def jump_attack(self, target):
        super().attack("jump attack", target, random.randint(500, 750))
