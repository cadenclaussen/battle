# Turn based healing via chance
# Turn based attack via chance
# Randomize number of players on each side?
# On each turn, randomize which player attacks first, second, ...
from Guardian import *
from Lynel import *
from Ganon import *

options = {
    "Gold Lynel 1": GoldLynel("Gold Lynel 1"),
    "Gold Lynel 2": GoldLynel("Gold Lynel 2"),
    "Silver Lynel 1": SilverLynel("Silver Lynel 1"),
    "Silver Lynel 2": SilverLynel("Silver Lynel 2"),
    "Silver Lynel 3": SilverLynel("Silver Lynel 3"),
    "Guardian 1": Guardian("Guardian 1"),
    "Guardian 2": Guardian("Guardian 2"),
    "Ganon": Ganon("Ganon")
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

def user_move(user, target):
    move_key = prompt("Choose a move", "Try again, that is not a valid move.", user.moves.keys())
    print()
    user.moves[move_key](target)

def bot_move(bot, target):
    move = random.choice(list(bot.moves.values()))
    move(target)
    print()

user_key = prompt("Choose a player", "Try again, that is not a valid player.", options)
user = options[user_key]
options.pop(user_key)

bot = random.choice(list(options.values()))

print()

while True:
    print("-" * 40)
    print("Battle: " + str(user) + " (you) vs. " + str(bot))
    print()
    user_move(user, bot)
    if bot.health <= 0:
        break

    bot_move(bot, user)
    if user.health <= 0:
        break

print()
print("-" * 40)
if user.health <= 0:
    print("You lose!")
else:
    print("You win!")
