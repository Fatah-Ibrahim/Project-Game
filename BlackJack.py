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


print('Weclome to Terminal BlackJack')
print('   Type start to begin  ')
begin_game = input().lower()

if begin_game == 'start':
    deck = Cards()
    card1 = deck.random_card()
    print(f'{card1[1]} of {card1[0]}')
    print('Hit        or   Stand. ')
else:
    exit()

choice1 = input().lower()
if choice1 == 'hit':
    deck = Cards()
    card2 = deck.random_card()
    print(f'{card1[1]} of {card1[0]}',"and",f'{card2[1]} of {card2[0]}')
    print('Hit        or   Stand. ')
else:
    pass


choice2 = input().lower()
if choice2 == 'hit':
    deck = Cards()
    card3= deck.random_card()
    print(f'{card1[1]} of {card1[0]}', f'{card2[1]} of {card2[0]}',f'{card3[1]} of {card3[0]}')

