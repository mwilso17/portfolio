import sys

import pygame

class SnowballFight:
  '''Main class to manage game'''

  def __init__(self):
    '''Initialize game'''
    pygame.init()

    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Snowball Fight")

    # Set background color
    self.bg_color = (50, 230, 100)

  def run_game(self):
    '''Runs the main loop for the game'''
    while True:
      # Detect keyboard and mouse events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      # Update screen during each loop
      self.screen.fill(self.bg_color)

      # Update to most recent screen.
      pygame.display.flip()


if __name__ == '__main__':
  # Make an instance of the game and run it.
  sf = SnowballFight()
  sf.run_game()
