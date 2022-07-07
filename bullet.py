import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        #get an attributes
        self.screen = ai_game.screen 
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color 
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width,
                                self.setting.bullet_height) 
        self.rect.midtop = ai_game.ship.rect.midtop #bullet position
        #store to float format
        self.y = float(self.rect.y) 
        self.x = float(self.rect.x)
        self.w = float(self.rect.w)
        
    def update(self):
        '''coordinate change'''
        self.y -= self.setting.bullet_speed #change the pos. of the bul.
        self.w += 0.4 #change the width of the bul,
        self.x -= 0.2 #correction x
        #update coordinate 
        self.rect.y = self.y 
        self.rect.w = self.w
        self.rect.x = self.x
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
                                
