import pygame
class Background():
      def __init__(self, ai_game):
            #get an attributes
            self.screen = ai_game.screen 
            self.bgimage = pygame.image.load('images/background.bmp')            
            #background scaling
            size = (ai_game.screen_width, ai_game.screen_height)
            self.bgimage = pygame.transform.scale(self.bgimage, size)
            #background rotated
            self.bgimage_rotated = pygame.transform.rotate(self.bgimage, 180)
            self.rectbimg = self.bgimage.get_rect()
            #coordinate background
            self.bgY1 = 0
            self.bgY2 = -self.rectbimg.height

            self.moving_speed = 0.15
         
      def update(self):
        '''changing the coordinates of the background insertion'''    
        self.bgY1 += self.moving_speed
        self.bgY2 += self.moving_speed
        if self.bgY1 >= self.rectbimg.height:
            self.bgY1 = -self.rectbimg.height
        if self.bgY2 >= self.rectbimg.height:
            self.bgY2 = -self.rectbimg.height
             
      def render(self):
         self.screen.blit(self.bgimage, (0, self.bgY1))
         self.screen.blit(self.bgimage_rotated, (0, self.bgY2))
