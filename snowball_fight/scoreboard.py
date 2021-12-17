import pygame.font
from pygame.sprite import Group

from snowman import Snowman

class Scoreboard:
  '''A class that stores and reports score information.'''

  def __init__(self, sf_game):
    '''Initialize score keeping.'''
    self.sf_game = sf_game
    self.screen = sf_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = sf_game.settings
    self.stats = sf_game.stats

    # Font settings and score info.
    self.text_color = (30, 30, 30)
    self.font = pygame.font.SysFont(None, 48)

    # Prep initial score image
    self.prep_score()
    self.prep_high_score()

    # Prep snowman images
    self.prep_snowmen()

  def prep_score(self):
    '''Turn the score into an image'''
    score_str = str(self.stats.score)
    self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

    # Display score in bottom right of screen
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 760

  def prep_high_score(self):
    '''Turn high score into an image'''
    high_score = round(self.stats.high_score)
    high_score_str = "{:,}".format(high_score)
    self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

    self.high_score_rect = self.high_score_image.get_rect()
    self.high_score_rect.centerx = self.screen_rect.centerx
    self.high_score_rect.top = self.score_rect.top

  def check_high_score(self):
    '''Check to see if there is a new high score'''
    if self.stats.score > self.stats.high_score:
      self.stats.high_score = self.stats.score
      self.prep_high_score()

  def prep_snowmen(self):
    '''Display lives left'''
    self.snowmen = Group()
    for snowman_number in range(self.stats.lives_left):
      snowman = Snowman(self.sf_game)
      snowman.rect.x = 10 + snowman_number * snowman.rect.width
      snowman.rect.y = 750
      self.snowmen.add(snowman)

  def show_score(self):
    '''Draw images to screen.'''
    self.screen.blit(self.score_image, self.score_rect)
    self.screen.blit(self.high_score_image, self.high_score_rect)
    self.snowmen.draw(self.screen)

