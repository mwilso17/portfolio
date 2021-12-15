import pygame.font

class Button:
  '''A class to store the button for Snowball Fight'''

  def __init__(self, sf_game, msg):
    '''Initialize button attributes'''
    self.screen = sf_game.screen
    self.screen_rect = self.screen.get_rect()

    # Set properties of button
    self.width, self.height = 200, 100
    self.button_color = (255, 255, 255)
    self.text_color = (30, 30 , 30)
    self.font = pygame.font.SysFont(None, 48)

    # Build button rect object and center it
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = self.screen_rect.center

    # Prep button one time
    self._prep_msg(msg)


  def _prep_msg(self, msg):
    '''Turn msg into rendered image and center on button.'''
    self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
    self.msg_image_rect = self.msg_image.get_rect()
    self.msg_image_rect.center = self.rect.center


  def draw_button(self):
    # Draw button and message
    self.screen.fill(self.button_color, self.rect)
    self.screen.blit(self.msg_image, self.msg_image_rect)
