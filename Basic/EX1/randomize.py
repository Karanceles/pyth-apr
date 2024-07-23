import random

# Moneda al aire
from random import choice
coin = choice(['cara','sello'])

# Random number
num_random = random.randint(1,10)

# Shuffle cartas
cards = ['Jack','Queen','King']
random.shuffle(cards)
for card in cards:
    print(card)

