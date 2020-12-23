import random

class Mob():
    name = ""
    health = 0
    initial_health = 0
    heal_multiplier = 0
    attacks = {}

    def __init__(self, name, health, heal_multiplier):
        self.name = name
        self.health = health
        self.initial_health = health
        self.heal_multiplier = heal_multiplier
        self.attacks = {}

    def attack(self, attack_name, target, damage):
        target.health -= damage
        if (target.health < 0):
            target.health = 0
        print(self.name + " attacked " + target.name + " using the " + attack_name + " attack (" + str(damage) + " damage) (" + target.name + " " + str(target.health) + ").")

    def heal(self):
        amount = random.randint(1, 5) * self.heal_multiplier
        self.health += amount
        if (self.health > self.initial_health):
            self.health = self.initial_health
        print(self.name + " healed (" + str(amount) + "/" + str(self.health) + ").")

    def __str__(self):
        return self.name + " (" + str(self.health) + ")"
