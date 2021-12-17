class Settings:
  '''This class stores the settings for Snowball Fight'''

  def __init__(self):
    '''Initialize game settings'''
    # Screen settings
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (50, 230, 100)

    # Snowman settings
    self.snowman_speed = 1
    self.lives_limit = 3

    # Snowball settings
    self.snowball_width = 10
    self.snowball_height = 10
    self.snowball_color = (255, 255, 255)


    # Game speed settings
    self.speedup_scale = 1.3

    self.initialize_dynamic_settings()

  def initialize_dynamic_settings(self):
    '''Settings for changes in difficulty'''
    self.snowball_speed = 1.0
    self.elf_frequency = 0.002
    self.elf_speed = 0.15
    self.snowballs_allowed = 2

  def increase_speed(self):
    '''Increases speed of dynamic settings'''
    self.snowball_speed *= self.speedup_scale
    self.elf_frequency *= self.speedup_scale
    self.elf_speed *= self.speedup_scale
    self.snowballs_allowed += 1