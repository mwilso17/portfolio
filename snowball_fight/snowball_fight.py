import sys
from random import random
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
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

    # Instant that stores game stats.
    self.stats = GameStats(self)

    self.snowman = Snowman(self)
    self.snowball = pygame.sprite.Group()
    self.elves = pygame.sprite.Group()

    # Make play button
    self.play_button = Button(self, 'Play')


  def run_game(self):
    '''Runs the main loop for the game'''
    while True:
      self._check_events()

      # Create new elf
      self._create_elves()

      if self.stats.game_active:
        self.snowman.update()
        self._update_snowballs()
        self._update_elves()

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

      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        self._check_play_button(mouse_pos)

  def _check_play_button(self, mouse_pos):
    '''Start a new game when Play is clicked'''
    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.stats.game_active:
      # Reset game settings.
      self.settings.initialize_dynamic_settings()

      # Reset game stats.
      self.stats.reset_stats()
      self.stats.game_active = True

      # Get rid of remaining objects on the screen.
      self.elves.empty()
      self.snowball.empty()

      # Reset screen to the start of the game.
      self._create_elves()
      self.snowman.ready_snowman()

      # Hide the mouse once 'start' is clicked
      pygame.mouse.set_visible(False)

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

    self._check_snowball_elf_collisions()

  def _update_elves(self):
    '''Update the position of all elves'''
    self.elves.update()

    # Decect when elf collides with snowman
    if pygame.sprite.spritecollideany(self.snowman, self.elves):
      self._snowman_hit()

    # Detect when elf reaches left side of screen
    self._check_elves_left()

  def _snowman_hit(self):
    '''Respond to snowman being hit by an elf'''
    if self.stats.lives_left > 0:
      # Reduce lives by 1
      self.stats.lives_left -= 1
    
      # delete any remaining field objects
      self.elves.empty()
      self.snowball.empty()

      # Redraw snowman and elves
      self._create_elves()
      self.snowman.ready_snowman()

      # Increase difficulty when hit
      self.settings.increase_speed()

      # Brief pause before movement starts
      sleep(1)
    else:
      self.stats.game_active = False
      pygame.mouse.set_visible(True)


  def _check_snowball_elf_collisions(self):
    '''Respond to bullet-elf collisions.'''

    # Check collisions and remove snowballs that have hit an elf
    collisions = pygame.sprite.groupcollide(self.snowball, self.elves, True, True)

  def _create_elves(self):
    '''Create the elves'''
    if random() < self.settings.elf_frequency:
      elf = Elf(self)
      self.elves.add(elf)


  def _check_elves_left(self):
    '''Check if elf has reached left side of screen. Delete elf if so.'''
    screen_rect = self.screen.get_rect()
    for elf in self.elves.sprites():
      if elf.rect.left <= 0:
        self.elves.remove(elf)

  def _update_screen(self):
    '''Update the images on the screen and flip to new screen'''
    # Update screen during each loop
    self.screen.fill(self.settings.bg_color)
    self.snowman.blitme()
    for snowball in self.snowball.sprites():
      snowball.draw_snowball()
    self.elves.draw(self.screen)

    # Draw play button when game is inactive
    if not self.stats.game_active:
      self.play_button.draw_button()

    # Update to most recent screen.
    pygame.display.flip()



if __name__ == '__main__':
  # Make an instance of the game and run it.
  sf = SnowballFight()
  sf.run_game()
