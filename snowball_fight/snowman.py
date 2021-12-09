import pygame

class Snowman:
  '''Class that manages the player character, aka: Snowman'''

  def __init__(self, sf_game):
    '''Initializes the Snowman and sets its starting point'''
    self.screen = sf_game.screen
    self.screen_rect = sf_game.screen.get_rect()

    # Load Snowman image and get its rect.
    self.image = pygame.image.load('snowball_fight\images\snowman.bmp')
    self.rect = self.image.get_rect()

    # Start each Snowman on the left middle of the screen.
    self.rect.midleft = self.screen_rect.midleft

  def blitme(self):
    '''Draw Snowman at its current location'''
    self.screen.blit(self.image, self.rect)