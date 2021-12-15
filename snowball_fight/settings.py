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
    self.snowball_speed = 1.0
    self.snowball_width = 10
    self.snowball_height = 10
    self.snowball_color = (255, 255, 255)
    self.snowballs_allowed = 2

    # Elf settings
    self.elf_speed = 0.15
    self.elf_frequency = 0.002