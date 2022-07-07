import random
import pygame
import sys
import json
from time import sleep
from ship import Ship
from setting import Settings
from background import Background
from bullet import Bullet
from alien import Alien
from game_stats import Game_stats
from button import Button
from scoreboard import Scoreboard
from laser import Laser
from bombs import Bomb

class Aliens():
    '''game class'''
    def __init__(self):
        pygame.init()
        #initialize the game screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
        self.screen_width = self.screen.get_rect().w
        self.screen_height = self.screen.get_rect().h
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Aliens')
        #create instances
        self.setting = Settings()
        self.game_stats = Game_stats(self)
        self.ship = Ship(self) 
        self.background = Background(self) 
        self.button = Button(self, 'Play')
        self.scoreboard = Scoreboard(self)
        #create groups
        self.bullets = pygame.sprite.Group() 
        self.aliens_group = pygame.sprite.Group()
        self.laser_group = pygame.sprite.Group()
        self.bomb_group = pygame.sprite.Group()
        self._create_fleet()
        #initialize random events
        delay = random.randint(4000, 7000)
        delay2 = random.randint(2000, 3000)
        delay3 = random.randint(3000, 5000)
        f_laser = pygame.USEREVENT
        f_bomb1 = pygame.USEREVENT + 1
        f_bomb2 = pygame.USEREVENT + 2
        pygame.time.set_timer(f_laser, delay)
        pygame.time.set_timer(f_bomb1, delay2)
        pygame.time.set_timer(f_bomb2, delay3)
        
    def run_game(self):
        '''main game loop'''
        while True: 
            self._check_events()
            if self.game_stats.game_active:
                self.ship.update()
                self._chek_fleet_edges()
                self._aliens_update()
                self._update_bullets()
                self._update_laser()
                self._update_bomb()
            self._update_screen()
            
    def _check_events(self):
        '''check keyboard and mouse events'''  
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self._json_dump()
                sys.exit()
            #random events
            if event.type == pygame.USEREVENT:
                self._fire_laser()
            if event.type == pygame.USEREVENT +1:
                self._fire_bomb()
            if event.type == pygame.USEREVENT +2:
                self._fire_bomb()
                
            elif event.type == pygame.KEYDOWN:
                self._check_keydow_events(event)                   
            elif event.type == pygame.KEYUP:
                self._check_keup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() #mouse click location
                self._check_play_button(mouse_pos)
                
    def _check_play_button(self, mouse_pos):
        '''button click test'''
        botton_clicked = self.button.rect.collidepoint(mouse_pos)
        if botton_clicked and not self.game_stats.game_active:
            self._start()
            
    def _start(self):
        '''initialization initial settings'''
        self.scoreboard.prep_ships()
        self.game_stats.reset_stats()
        self.setting.initialize_dynamic_settings()
        self.game_stats.game_active = True
        self.scoreboard.prep_scrore()
        self.aliens_group.empty()
        self.bullets.empty()
        self.bomb_group.empty()
        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)
        
    def _check_keydow_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True #traffic flag
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self._json_dump() #save hight score
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.game_stats.game_active:
            self._start()
            
    def _check_keup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        if len(self.bullets) < self.setting.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        '''bullet movement and bullets removal'''
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._chek_bullet_alien_collision()
        
    def _update_screen(self):
        self.background.update() #changing the background drawing coordinates
        self.background.render() #drawing a dynamic background
        self.ship.blitme()
        self.aliens_group.draw(self.screen)
        self.scoreboard.show_score()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for laser in self.laser_group.sprites():
            laser.draw_laser()
        for bomb in self.bomb_group.sprites():
            bomb.draw_bomb()
        if not self.game_stats.game_active:
            self.button.draw_button()
        pygame.display.flip() #last rendered screen
        
    def _create_fleet(self):
        '''preparation for drawing the fleet and calculating
        the number of aliens'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.screen_width - (2 * alien_width)
        available_space_y = (self.screen_height -
                             (3 * alien_height) - self.ship.rect.height)
        number_aliens_x = available_space_x // (2 * alien_width) 
        number_aliens_y = available_space_y // (2 * alien_height)
        for number_y in range(number_aliens_y):
            for number_x in range(number_aliens_x):
                self._create_alien(number_x, number_y)
                
    def _create_alien(self, number_x, number_y):
        '''creating a fleet by coordinates'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * number_x  
        alien.y = alien_height + 1.3 * alien_width * number_y - 30
        alien.rect.x, alien.rect.y = alien.x, alien.y
        self.aliens_group.add(alien)
                
    def _aliens_update(self):
        '''fleet movement and collision check'''
        self.aliens_group.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens_group): 
            self._ship_hit()
        self._check_aliens_bottom()
        
    def _chek_fleet_edges(self):
        '''#changing the direction of the fleet'''
        for alien in self.aliens_group.sprites():
            if alien.chek(): 
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        '''change direction and fleet drop'''
        for alien in self.aliens_group.sprites():
            alien.rect.y += self.setting.fleet_y_speed
        self.setting.fleet_direction *= -1 #change of direction
        
    def _chek_bullet_alien_collision(self):
        '''Destroying aliens and updating statistics. If there are
        no aliens left, then we move on to a new level'''
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens_group, True, True) 
        if collisions:
            for alien in collisions.values():
                self.game_stats.score += self.setting.alien_point * len(alien)
            self.scoreboard.prep_scrore()
            self.scoreboard.check_hight_score()
        if not self.aliens_group:
            self.bullets.empty()
            self._create_fleet()
            self.setting.increase_speed()
            self.game_stats.level += 1
            self.scoreboard.prep_level()
            
    def _ship_hit(self):
        '''ship destruction and game update'''
        if self.game_stats.ships_left > 0: 
            self.game_stats.ships_left -=1
            self.scoreboard.prep_ships()
            self.bullets.empty()
            self.aliens_group.empty()
            self.laser_group.empty()
            self.bomb_group.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(1)
        else:
            self.game_stats.game_active = False
            pygame.mouse.set_visible(True)
            
    def _check_aliens_bottom(self):
        '''checking the aliens reach the bottom of the screen'''
        for alien in self.aliens_group.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_hit()
                break
            
    def _update_laser(self):
        '''laser movement, removal and ship damage check'''
        self.laser_group.update(self)
        for laser in self.laser_group.copy():
            if laser.rect.top > self.screen_rect.h:
                self.laser_group.remove(laser)
        if pygame.sprite.spritecollideany(self.ship, self.laser_group): 
            self._ship_hit()
            
    def _fire_laser(self):
        '''random alien laser attack'''
        alien_list = []
        for alien in self.aliens_group:
            alien_list.append(alien)
        self.random_alien = random.choice(alien_list)
        laser = Laser(self)
        self.laser_group.add(laser)
        
    def _update_bomb(self):
        '''bombs movement, removal and ship damage check'''
        self.bomb_group.update()
        for bomb in self.bomb_group.copy():
            if bomb.rect.top > self.screen_rect.h:
                self.bomb_group.remove(bomb)
        if pygame.sprite.spritecollideany(self.ship, self.bomb_group): 
            self._ship_hit()
            
    def _fire_bomb(self):
        '''random alien bomb attack'''
        alien_list = []
        for alien in self.aliens_group:
            alien_list.append(alien)
        self.random_alien2 = random.choice(alien_list)
        bomb = Bomb(self)
        self.bomb_group.add(bomb)
        
    def _json_dump(self):
        with open('hight_score.json', 'w') as hs:
            json.dump(self.game_stats.hight_score, hs)            

ai = Aliens()
ai.run_game()
