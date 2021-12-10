import pygame
from pygame.sprite import Sprite

class Snowball(Sprite):
  '''Class manages snowball projectiles'''

  def __init__(self, sf_game):
    '''Create snowball object'''
    super().__init__()
    self.screen = sf_game.screen
    self.settings = sf_game.settings
    self.color = self.settings.snowball_color

    # Create a snowball and set its position
    self.rect = pygame.Rect(0, 0, self.settings.snowball_width, self.settings.snowball_height)
    self.rect.midleft = sf_game.snowman.rect.midleft

    # Store snowball position as decimal value
    self.x = float(self.rect.x)

  def update(self):
    '''Fires snowball to the right'''
    self.x += self.settings.snowball_speed
    
    # Update rect position
    self.rect.x = self.x

  def draw_snowball(self):
    '''Draw snowball to the screen'''
    pygame.draw.rect(self.screen, self.color, self.rect)