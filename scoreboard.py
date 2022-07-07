import pygame.font
from pygame.sprite import Group
from shipleft import Ship

class Scoreboard():
    def __init__(self, ai_game):
        #get an attributes
        self.ship = ai_game.ship
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.setting = ai_game.setting
        self.game_stats = ai_game.game_stats

        self.text_color = (255, 0, 255)
        self.font = pygame.font.SysFont(None, 48) #font preparation

        self.prep_scrore()
        self.high_score()
        self.prep_level()
        self.prep_ships()

    def prep_scrore(self):
        '''convert score to images'''
        score_str = '{:,}'.format(self.game_stats.score)
        score_str = f'score {score_str}'
        self.score_image = self.font.render(score_str, True, self.text_color,
                                          self.setting.bg_color)
        self.score_image.set_colorkey((0, 0, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def high_score(self):
        '''convert high score to images'''
        hight_score_str = '{:,}'.format(self.game_stats.hight_score)
        hight_score_str = f'hight {hight_score_str}'
        self.hight_score_image = self.font.render(hight_score_str, True, self.text_color,
                                          self.setting.bg_color)
        self.hight_score_image.set_colorkey((0, 0, 0))
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx 
        self.hight_score_rect.y = 20
        
    def prep_level(self):
        '''convert level to images'''
        level_str = f'lev. {self.game_stats.level}'
        self.level_image = self.font.render(level_str, True, self.text_color,
                                          self.setting.bg_color)
        self.level_image.set_colorkey((0, 0, 0))
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.hight_score_image,
                         self.hight_score_rect)
        self.ships.draw(self.screen)
        
    def check_hight_score(self):
        if self.game_stats.score > self.game_stats.hight_score:
            self.game_stats.hight_score = self.game_stats.score
            self.high_score() #update method def high_score
            
    def prep_ships(self):
        '''display the image of the remaining lives in the form of ships'''
        self.ships = pygame.sprite.Group()
        for ship_numb in range(self.game_stats.ships_left):
            ship = Ship()                        
            ship.rect.x = 5 + ship_numb * ship.rect.w
            ship.rect.y = 5
            self.ships.add(ship)
    
        
            
        
        
