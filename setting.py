from alien import Alien
class Settings():
    def __init__(self):
        self.bg_color = (0, 0, 0)                
        self.ship_speed = 3
        self.ship_limit = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.laser_color = (255, 255, 0)
        self.bomb_color = (0, 255, 0)
        self.bullets_allowed = 3
        self.fleet_y_speed = 40
        self.laser_speed = 2
        
        self.speedup_scale = 1.3 #rate of change of speed
        self.point_scale = 1.5 #rate of change of point
        
    def initialize_dynamic_settings(self):
        '''settings that change with the new level'''
        self.fleet_direction = 1 #direction of movement of aliens (1 right)
        self.alien_speed = 0.2
        self.bullet_speed = 1.5
        self.alien_point = 50
        self.bomb_speed = 1.5

    def increase_speed(self):
        '''increase dynamic_settings'''
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.laser_speed *= self.speedup_scale
        self.bomb_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.point_scale)
        
        
