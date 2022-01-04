# Mike Wilson 4 Jan 2022
# This program uses random to help generate a character for a tabletop RPG.
from random import randint
import math

# Core stats: strength, dexterity, constitution, intelligence, wisdom, charisma
class Character():
  '''Overall class to manage a player character.'''

  def __init__(self):
    '''initialize new character.'''
    self.generate_stats()

  def generate_stats(self):
    '''Use random to generate stats and print them.'''
    strength = randint(1, 20)
    dexterity = randint(1, 20)
    constitution = randint(1, 20)
    intelligence = randint(1, 20)
    wisdom = randint(1, 20)
    charisma = randint(1, 20)
    hit_points = math.ceil(randint(1, 9) + constitution/5)

    print("Strength: " + str(strength))
    print("Dexterity: " + str(dexterity))
    print("Constitution: " + str(constitution))
    print("Intelligence: " + str(intelligence))
    print("Wisdom: " + str(wisdom))
    print("Charisma: " + str(charisma))
    print("Hit Points: " + str(hit_points))


player1 = Character()
