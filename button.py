import pygame.font
class Button():
    def __init__(self, ai_game, msg):
        #get an attributes
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen_rect

        self.button_color = (255, 0, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) #font preparation

        self.rect = pygame.Rect(0, 0, 200, 50) 
        self.rect.center = self.screen_rect.center #button position

        self._prep_msg(msg) #get an attribute of creat message
        
    def _prep_msg(self, msg):
        '''creating a button message'''
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
       pygame.draw.rect(self.screen, self.button_color, self.rect) 
       self.screen.blit(self.msg_image, self.msg_image_rect)
