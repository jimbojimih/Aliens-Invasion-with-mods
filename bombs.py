import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        #get an attributes
        self.screen = ai_game.screen 
        self.setting = ai_game.setting 
        self.color = self.setting.bomb_color
        
        self.rect = pygame.Rect(0, 0, 15, 15) 
        self.rect.midtop = ai_game.random_alien2.rect.midbottom  #bomb position
        self.y = float(self.rect.y) #store to float format
        
    def update(self):
        '''coordinate change'''
        self.y += self.setting.bomb_speed
        self.rect.y = self.y
        
    def draw_bomb(self):
        pygame.draw.rect(self.screen, self.color, self.rect)



