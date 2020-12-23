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
        self.moves = { "heal": self.heal }

    def attack(self, attack_name, target, damage):
        target.health -= damage
        print(self.name + " performed a " + attack_name + " attack on " + target.name + " doing " + str(damage) + " points of damage.")

    # Note: because the consumer always passes the target, we must accept
    # it, however, heal doesn't care about the target, so it is ignored
    # in this case.
    def heal(self, target):
        amount = random.randint(1, 5) * self.heal_multiplier
        self.health += amount
        if (self.health > self.initial_health):
            self.health = self.initial_health
        print(self.name + " healed " + str(amount) + " points of damage.")

    def status(self):
        print(self.name + "'s health is " + str(self.health) + "points.")

    def __str__(self):
        return self.name + " (" + str(self.health) + ")"
