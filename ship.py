import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        #get an attributes
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen_rect 
        self.setting = ai_game.setting

        self.image = pygame.image.load('images/shipBlack.bmp')
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect() 
        #ship position
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.height - 10 

        self.x = float(self.rect.x) #store to float format
        #move flags
        self.moving_right = False 
        self.moving_left = False
        
    def update(self):
        '''coordinate change and screen exit check'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        self.rect.x = self.x # update coordinate x
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        '''put the ship in the starting position'''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.height - 10
        self.x = float(self.rect.x)
        
    
