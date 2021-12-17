import pygame

class Snowman:
  '''Class that manages the player character, aka: Snowman'''

  def __init__(self, sf_game):
    '''Initializes the Snowman and sets its starting point'''
    self.screen = sf_game.screen
    self.settings = sf_game.settings
    self.screen_rect = sf_game.screen.get_rect()

    # Load Snowman image and get its rect.
    self.image = pygame.image.load('snowball_fight\images\snowman.bmp')
    self.rect = self.image.get_rect()

    # Start each Snowman on the left middle of the screen.
    self.rect.midleft = self.screen_rect.midleft

    # Store a decimal value for Snowman's vertical positioning
    self.y = float(self.rect.y)

    # Movement flags
    self.moving_up = False
    self.moving_down = False

  def update(self):
    '''Update Snowman's location based on movement flags'''
    # Update Snowman's y value
    if self.moving_up and self.rect.top >= 0:
      self.y -= self.settings.snowman_speed
    if self.moving_down and self.rect.bottom < self.screen_rect.bottom - 50:
      self.y += self.settings.snowman_speed

    # Update rect object from self.y
    self.rect.y = self.y

  def blitme(self):
    '''Draw Snowman at its current location'''
    self.screen.blit(self.image, self.rect)

  def ready_snowman(self):
    '''Center snowman to left of screen'''
    self.rect.midleft = self.screen_rect.midleft
    self.y = float(self.rect.y)