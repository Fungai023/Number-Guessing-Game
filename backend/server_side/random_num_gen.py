import random

class GuessNumGenarator():

    def __init__(self, guess_length , range_length):
        self.guess_length = guess_length
        self.range_length = range_length
        self.guess_list = []


    def random_number(self):
        for num  in range(self.guess_length):
            random_num = random.randint(self.range_length)
            self.guess_list.__add__(random_num)
        return self.guess_list
    
    def string_guess(self):
        num_list= self.guess_list
        
            
