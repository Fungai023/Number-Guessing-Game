import random

class GuessNumGenarator():
    guess_list = []
    guess = ""
    def __init__(self, guess_length , range_length):
        self.guess_length = guess_length
        self.range_length = range_length
        


    def random_number(self):
        for num  in range(self.guess_length):
            random_num = random.randint(self.range_length)
            self.guess_list.__add__(random_num)
      
    
    def string_guess(self):
        word = ",".join(self.guess_list)
        self.guess += word
    

    # def is_guess_correct():
        
        
            
