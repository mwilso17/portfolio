class GameStats:
  '''Track stats for Snowball Fight'''

  def __init__(self, sf_game):
    '''Initialize statistics'''
    self.settings = sf_game.settings
    self.reset_stats()

  def reset_stats(self):
    '''Initialize in game stats'''
    self.lives_left = self.settings.lives_limit