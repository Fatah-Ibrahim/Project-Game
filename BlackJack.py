#Hello guys. What game are we doing?
import random

# deck = Cards()
# print(deck.random_card())
class Cards:
    def __init__(self):
        self.card_type = ['Spades', 'Clover', 'Heart', 'Diamonds']
        self.card_num = [2,3,4,5,6,7,8,9,10,'K', 'Q', 'J', 'A']
        # self.special_cards = special_cards
        
    def get_card_type(self):
        return self.card_type
    
    def set_card_type(self,card):
        self.card_type = card
    
    def get_card_num(self):
        return self.card_num
    
    def random_card(self):
        card_type = random.choice(self.card_type)
        card_num = random.choice(self.card_num)
        combined_card = [card_num, card_type]
        return combined_card

