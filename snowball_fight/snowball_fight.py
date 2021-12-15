import sys
from random import random

import pygame

from settings import Settings
from snowman import Snowman
from snowball import Snowball
from elf import Elf

class SnowballFight:
  '''Main class to manage game'''

  def __init__(self):
    '''Initialize game'''
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    pygame.display.set_caption("Snowball Fight")

    self.snowman = Snowman(self)
    self.snowball = pygame.sprite.Group()
    self.elves = pygame.sprite.Group()


  def run_game(self):
    '''Runs the main loop for the game'''
    while True:
      self._check_events()

      # Create new elf
      self._create_elves()

      self.snowman.update()
      self._update_snowballs()
      self.elves.update()
      self._update_screen()

  def _check_events(self):
    '''Detect keystrokes and mouse events'''
    # Detect keyboard and mouse events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)

      elif event.type == pygame.KEYUP:
        self._check_keyup_events(event)

  def _check_keydown_events(self, event):
    '''Respond to keypresses'''
    if event.key == pygame.K_UP:
      self.snowman.moving_up = True
    elif event.key == pygame.K_DOWN:
      self.snowman.moving_down = True
    elif event.key == pygame.K_q:
      sys.exit()
    elif event.key == pygame.K_SPACE:
      self._throw_snowball()

  def _check_keyup_events(self, event):
    '''Respond to key releases'''
    if event.key == pygame.K_UP:
      self.snowman.moving_up = False
    elif event.key == pygame.K_DOWN:
      self.snowman.moving_down = False

  def _throw_snowball(self):
    '''Create a new snowball and add it to the snowball group'''
    if len(self.snowball) < self.settings.snowballs_allowed:
      new_snowball = Snowball(self)
      self.snowball.add(new_snowball)

  def _update_snowballs(self):
    '''Update psoition of snowballs and get rid of old ones'''
    self.snowball.update()

    # Get rid of off screen snowballs
    for snowball in self.snowball.copy():
      if snowball.rect.left >= self.settings.screen_width:
        self.snowball.remove(snowball)

  def _create_elves(self):
    '''Create the elves'''
    if random() < self.settings.elf_frequency:
      elf = Elf(self)
      self.elves.add(elf)
      print(len(self.elves))

  def _update_screen(self):
    '''Update the images on the screen and flip to new screen'''
    # Update screen during each loop
    self.screen.fill(self.settings.bg_color)
    self.snowman.blitme()
    for snowball in self.snowball.sprites():
      snowball.draw_snowball()
    self.elves.draw(self.screen)

    # Update to most recent screen.
    pygame.display.flip()



if __name__ == '__main__':
  # Make an instance of the game and run it.
  sf = SnowballFight()
  sf.run_game()
