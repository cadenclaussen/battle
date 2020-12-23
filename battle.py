from Guardian import *
from Lynel import *
from Ganon import *
from Link import *

options = {
    "Gold Lynel 1": GoldLynel("Gold-Lynel-1"),
    "Gold Lynel 2": GoldLynel("Gold-Lynel-2"),
    "Silver Lynel 1": SilverLynel("Silver-Lynel-1"),
    "Silver Lynel 2": SilverLynel("Silver-Lynel-2"),
    "Silver Lynel 3": SilverLynel("Silver-Lynel-3"),
    "Guardian 1": Guardian("Guardian-1"),
    "Guardian 2": Guardian("Guardian-2"),
    "Ganon": Ganon("Ganon"),
    "Link": Link("Link")
}

def prompt(prefix, error, options):
    print(prefix + ": ")

    # Create a dictionary like this:
    # {
    #     "1": "option 1"
    #     "2": "option 2"
    #     ...
    # }
    option_numbers = {}
    i = 1
    for option in options:
        option_numbers[str(i)] = option
        i += 1

    # Print out the user's options
    for option_number in option_numbers:
        print(str(option_number) + ") " + option_numbers[option_number])

    # Get the user's response, if incorrect, error, and reprompt
    number = input("> ").strip()
    while number not in list(option_numbers.keys()):
        print(error)
        number = input("> ").strip()

    return option_numbers[number]

def chance(percent):
    if (random.randint(0, 100) <= percent):
        return True
    return False

def battle():

    # Prompt the player for which player they want to use
    user_key = prompt("Choose a player", "Try again, that is not a valid player.", options)
    user = options[user_key]
    options.pop(user_key)

    # Randomly pick a bot from the remaining characters
    bot = random.choice(list(options.values()))

    print("Battle: " + str(user) + " (you) vs. " + str(bot))
    print()
    while True:
        print("-" * 40)

        # attack_key = prompt("Choose an attack", "Try again, that is not a valid attack.", user.attacks.keys())
        if (chance(50)):
            attack_key = random.choice(list(user.attacks.keys()))
            user.attacks[attack_key](bot)
            if bot.health <= 0:
                print(bot.name + ' died.')
                break

        if (chance(50)):
            attack_function = random.choice(list(bot.attacks.values()))
            attack_function(user)
            if user.health <= 0:
                print(user.name + ' died.')
                break

        if (chance(40)):
            user.heal()

        if (chance(30)):
            bot.heal()

    print("-" * 40)
    if user.health <= 0:
        print("You lose!")
    else:
        print("You win!")



battle()
