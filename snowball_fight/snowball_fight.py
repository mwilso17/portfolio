import sys

import pygame

from settings import Settings

class SnowballFight:
  '''Main class to manage game'''

  def __init__(self):
    '''Initialize game'''
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    pygame.display.set_caption("Snowball Fight")


  def run_game(self):
    '''Runs the main loop for the game'''
    while True:
      # Detect keyboard and mouse events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      # Update screen during each loop
      self.screen.fill(self.settings.bg_color)

      # Update to most recent screen.
      pygame.display.flip()


if __name__ == '__main__':
  # Make an instance of the game and run it.
  sf = SnowballFight()
  sf.run_game()
