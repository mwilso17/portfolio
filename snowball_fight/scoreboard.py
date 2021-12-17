import pygame.font

class Scoreboard:
  '''A class that stores and reports score information.'''

  def __init__(self, sf_game):
    '''Initialize score keeping.'''
    self.screen = sf_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = sf_game.settings
    self.stats = sf_game.stats

    # Font settings and score info.
    self.text_color = (30, 30, 30)
    self.font = pygame.font.SysFont(None, 48)

    # Prep initial score image
    self.prep_score()

  def prep_score(self):
    '''Turn the score into an image'''
    score_str = str(self.stats.score)
    self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

    # Display score in bottom right of screen
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 760

  def show_score(self):
    '''Draw score to screen.'''
    self.screen.blit(self.score_image, self.score_rect)
