import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        #get an attributes
        self.screen = ai_game.screen 
        self.setting = ai_game.setting 
        self.color = self.setting.laser_color
        
        self.rect = pygame.Rect(0, 0, 10, 1) 
        self.rect.midtop = ai_game.random_alien.rect.midbottom #laser position
        self.y = float(self.rect.h) #store to float format
        self.y2 = float(self.rect.y) 
                
    def update(self, ai_game):
        '''coordinate change'''
        self.y += self.setting.laser_speed
        self.rect.centerx = ai_game.random_alien.rect.centerx #align the laser
        if self.rect.h < 500: #increaser the height of the reactangle
            self.rect.h = self.y 
        else:
            self.y2 += self.setting.laser_speed #change the pos. of the laser
            self.rect.y = self.y2

    def draw_laser(self):
        pygame.draw.rect(self.screen, self.color, self.rect)




                                
