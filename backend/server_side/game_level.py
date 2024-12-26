class GameLevel():
 
    def __init__(self, level,win  , num_length , guess_range ):
        self.level = level
        self.win =  win
        self.num_length = num_length
        self.guess_range = guess_range
        
    def get_level(self):
        return self.level
    
    def get_win_boolean(self):
        return self.win
    
    def get_num_length(self):
        return self.num_length
    
    def get_guess_range(self):
        return self.guess_range

    def level_Updater(self):
          if self.win :
            self.level += 1
            
#learn the art of mathematical progression
    def level_checker(self):
        if self.level % 5 == 0 :
            if self.level < 10 and self.level > 5 :
                self.guess_range


         
        
    
