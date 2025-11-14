#Hello guys. What game are we doing?
import random

# deck = Cards()
# print(deck.random_card())
class Cards:
    def __init__(self):
        self.card_type = ['Spades', 'Clover', 'Heart', 'Diamonds']
        self.card_num = ['2','3','4','5','6','7','8','9','10','K', 'Q', 'J', 'A']
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
    
    def hand_value(hand):
        value=0
        ace=0
        for card in hand:
            num =card[0] 
            if num in ['K','Q','J']:
                value+=10
            elif num=='A':
                value+=11
                ace+=1
            else:
                value+=int(num)
        while value>21 and ace>0:
            value -=10
            aces-=1
        return value


print('Weclome to Terminal BlackJack')
print('   Type start to begin  ')
begin_game = input().lower()

if begin_game == 'start':
    deck = Cards()
    card1 = deck.random_card()
    print(f'{card1[0]} of {card1[1]}')
    print('Hit        or   Stand. ')
else:
    exit()

choice1 = input().lower()
if choice1 == 'hit':
    card2 = deck.random_card()
    print(f'{card1[0]} of {card1[1]}',"and",f'{card2[0]} of {card2[1]}')
    print('Hit        or   Stand. ')
else:
    print("You choose to stand")


choice2 = input().lower()
if choice2 == 'hit':
    card3= deck.random_card()
    print(f'{card1[0]} of {card1[1]}, {card2[0]} of {card2[1]}, {card3[0]} of {card3[1]}')
else:
    print("You choose to stand")
