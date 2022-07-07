import json
class Game_stats():
    def __init__(self, ai_game):
        #get an attributes
        self.setting = ai_game.setting 
        self.open_hight_score() 
        self.reset_stats()
        self.game_active = False #game active flag
        
    def reset_stats(self):
        self.ships_left = self.setting.ship_limit
        self.score = 0
        self.level = 1
        
    def open_hight_score(self):
        with open('hight_score.json') as hs:
            self.hight_score = json.load(hs)
