from random import randint

import pygame
from pygame.sprite import Sprite

class Elf(Sprite):
  '''Class that represents individual elf.'''

  def __init__(self, sf_game):
    '''Initialize elf and set its starting location.'''
    super().__init__()
    self.screen = sf_game.screen
    self.settings = sf_game.settings

    # Load image and set its rect
    self.image = pygame.image.load('snowball_fight\images\elf.bmp')
    self.rect = self.image.get_rect()

    # Start new elves at random locations on the right side of the screen
    self.rect.left = self.screen.get_rect().right

    # Limit placement of elves
    elf_top_max = self.settings.screen_height - 60
    self.rect.top = randint(0, elf_top_max)

    # Store elf's position.
    self.x = float(self.rect.x)

  def update(self):
    '''Move elf'''
    self.x -= self.settings.elf_speed
    self.rect.x = self.x