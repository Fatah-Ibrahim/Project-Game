#Hello guys. What game are we doing?
import random

# got from google to clear the terminal to easier user interface
import os


def clear_terminal():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


class Cards:
    def __init__(self):
        self.card_type = ('Spades', 'Clover', 'Heart', 'Diamonds')
        self.card_num = ('2','3','4','5','6','7','8','9','10','K', 'Q', 'J', 'A')

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


class Player:
    def __init__(self, name, balance = 1000, hand = []):
        self.name = name
        self.balance = balance
        self.hand = hand
    
    def add_card(self):
        self.hand.append(deck.random_card())
        self.hand.append(deck.random_card())
        


# bank account and betting system
class Bank:
    def __init__(self, balance = 1000):
        self.balance = balance

    def bet(self, amount):
        amount = int(amount)
        if amount > self.balance:
            return False
        self.balance -= amount
        return amount
    
    def win(self, amount):
        self.balance += int(amount)

    def lose(self, amount):
        self.balance -= int(amount)

    def tie(self):
        pass

    def show(self):
        return self.balance

# gives the card nums value as a point system
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
        ace-=1
    return value

balance = Bank(1000)
print('Weclome to Terminal BlackJack')
print()
print('   Type start to begin  ')
print()

begin_game = input().lower()


# if statement to start the game
if begin_game == 'start':
    clear_terminal()

    print('How much are you will to bet')
    print()
    print(f'Balance: ${balance.show()}')
    print()
    bet1 = balance.bet(input())
    if bet1 == False:
        print('Insufficient Funds')
        quit()


    clear_terminal()

    deck = Cards()
    player_hand = []
    dealer_hand = []

    # adding to the player deck and dealer deck
    player_hand.append(deck.random_card())
    player_hand.append(deck.random_card())
    dealer_hand.append(deck.random_card())
    dealer_hand.append(deck.random_card())


    print(f'Your new hand:')
    for card in player_hand:
        print(f'{card[0]} of {card[1]}')
    print(f'Total: {hand_value(player_hand)}')


# trying to show dealers first card with showing second card too
    '''for card in dealer_hand:
        for card in range(0, dealer_hand):
            print(f'{card[0]} of {card[1]}')'''



#Player's turn
while hand_value(player_hand) < 21:
    choice = input("'hit or stand?").lower()
    
    if choice == 'hit':
        clear_terminal()
        player_hand.append(deck.random_card())
    
        print(f'Your hand:')
        for card in player_hand:
            print(f'{card[0]} of {card[1]}',)
        print(f"Total: {hand_value(player_hand)}")

    if hand_value(player_hand) > 21:
        print('You Bust! Dealer Wins')
        break

    elif choice == 'stand':
        print('You choose to stand\n')
        break

#dealers turn 
while hand_value(dealer_hand)<17:
    clear_terminal
    dealer_hand.append(deck.random_card())
    print('Dealers Turn')

    for card in dealer_hand:
        print(f'{card[0]} of {card[1]}')
print(f'Total: {hand_value(dealer_hand)}')

player_total=hand_value(player_hand)
dealer_total=hand_value(dealer_hand)

print('\n Result   ')
print()

if dealer_total > 21:
    print('Dealer Bust! You win!')
    balance.win(bet1 * 2)

elif player_total > 21:
    print('You Bust! Dealer Wins')


elif player_total > dealer_total:
    print('You win')
    balance.win(bet1 * 2)

elif player_total < dealer_total:
    print('Dealer wins')

else:
    print('Tie')
    balance.win(bet1)

print()
print(f'Current balance: ${balance.show()}')
