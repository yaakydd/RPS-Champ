# This is the main entry point of the project
from game import play, poki, roki, groki, woki, human, random_player
from rock_pasci import player
from unittest import main

play(player, groki, 1000)
play(player, roki, 1000)
play(player, woki, 1000)
play(player, poki, 1000)

# Uncomment line below to play interactively against a bot:
play(human, roki, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)

# Uncomment line below to run unit tests automatically
#main(module='test_module', exit=False)
