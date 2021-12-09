import sys

import pygame

from settings import Settings
from snowman import Snowman

class SnowballFight:
  '''Main class to manage game'''

  def __init__(self):
    '''Initialize game'''
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    pygame.display.set_caption("Snowball Fight")

    self.snowman = Snowman(self)


  def run_game(self):
    '''Runs the main loop for the game'''
    while True:
      self._check_events()
      self.snowman.update()
      self._update_screen()

  def _check_events(self):
    '''Detect keystrokes and mouse events'''
    # Detect keyboard and mouse events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          self.snowman.moving_up = True
        elif event.key == pygame.K_DOWN:
          self.snowman.moving_down = True


      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          self.snowman.moving_up = False
        elif event.key == pygame.K_DOWN:
          self.snowman.moving_down = False

  def _update_screen(self):
    '''Update the images on the screen and flip to new screen'''
    # Update screen during each loop
    self.screen.fill(self.settings.bg_color)
    self.snowman.blitme()

    # Update to most recent screen.
    pygame.display.flip()



if __name__ == '__main__':
  # Make an instance of the game and run it.
  sf = SnowballFight()
  sf.run_game()
