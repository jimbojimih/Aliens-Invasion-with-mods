import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''initializes the enemy'''
    def __init__(self, ai_game):
        super().__init__()
        #get an attributes
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect() 
        self.setting = ai_game.setting 

        self.image = pygame.image.load('images/alien1.bmp') 
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect() 

        self.x = float(self.rect.x) #store to float format

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''move update'''
        self.x += self.setting.alien_speed * self.setting.fleet_direction
        self.rect.x = self.x # update coordinate x
        
    def chek(self):
        '''screen exit check'''
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
    
