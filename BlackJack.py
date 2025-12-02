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
    
    def __str__(self):
        return f"{self.card_type}, {self.card_num}"

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
    
    def __str__(self):
        return f"{self.balance}"

class Player:
    def __init__(self, name, balance = 1000):
        self.name = name
        self.balance = balance
        self.hand = []
    
    def add_card(self,deck):
        self.hand.append(deck.random_card())
    
    def __str__(self):
        return f"{self.name}, {self.balance}"

player_name = input("Enter your name: ")

def load_balance(file_name,player_name,default_balance=1000):
    try:
        with open(file_name,"r") as game_data:
            data=game_data.readlines()
    # Making new file if file doesnt exist
    except FileNotFoundError:
        data=[]

    #returns the saved balance if the player is found
    for line in data:
        name,balance=line.split(',')
        if name == player_name:
            return int(balance),data
    #makes a new line if player is not found
    with open(file_name, 'a') as game_data:
        game_data.write(f"{player_name}, {Bank.balance()}\n")

    data.append(f"{player_name},{Bank.balance()}\n")
    return {Bank.balance()},data


def update_balance(file_name,player_name,new_balance,data):
    new_data=[]
    update=False

    for line in data:
        name,balance=line.split(',')
        #if player found this replaces the old balance with the new balance
        if name == player_name:
            new_data.append(f"{player_name},{new_balance}\n")
            update=True
        else:
            new_data.append(line)
    #add the player if the are not already in the file
    if not update:
        new_data.append(f"{player_name},{new_balance}\n")
    
    with open(file_name, "w") as game_data:
        game_data.writelines(new_data)


balance_amount, data = load_balance("BlackJack.txt", player_name,)
balance = Bank(balance_amount)

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
print('Welcome to Terminal BlackJack')
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
    bet_amount = int(input())
    bet1 = balance.bet(bet_amount)
    if bet1 == False:
        print('Insufficient Funds')
        quit()


    clear_terminal()

    deck = Cards()
    player_1 = Player(player_name)
    player_2 = Player('Dealer', float('inf'))

    # adding to the player deck and dealer deck
    player_1.add_card(deck)
    player_1.add_card(deck)
    player_2.add_card(deck)
    player_2.add_card(deck)


    print(f'Your new hand:')
    for card in player_1.hand:
        print(f'{card[0]} of {card[1]}')
    print(f'Total: {hand_value(player_1.hand)}')

    print("\nDealer's hand:")
    print(f'{player_2.hand[0][0]} of {player_2.hand[0][1]}')
    print("Second card is hidden\n")


# trying to show dealers first card with showing second card too



#Player's turn
while hand_value(player_1.hand) < 21:
    choice = input("'hit or stand?").lower()
    
    if choice == 'hit':
        clear_terminal()
        player_1.add_card(deck)
    
        print(f'Your hand:')
        for card in player_1.hand:
            print(f'{card[0]} of {card[1]}',)
        print(f"Total: {hand_value(player_1.hand)}")

    if hand_value(player_1.hand) > 21:
        print('You Bust! Dealer Wins')
        break
            
    elif choice == 'stand':
        print('You choose to stand\n')
        break

#dealers turn 
while hand_value(player_2.hand)<17:
    player_2.add_card(deck)
    
#kskjdsdoklsd
print('Dealers Final Hand:')
for card in player_2.hand:
    print(f'{card[0]} of {card[1]}')
print(f'Total: {hand_value(player_2.hand)}')

player_total=hand_value(player_1.hand)
dealer_total=hand_value(player_2.hand)

print('\n Result   ')
print()

if dealer_total > 21:
    print('Dealer Bust! You win!')
    balance.win(bet1 * 2)

elif player_total ==21:
    print('You Bust! Dealer Wins')

elif player_total >21:
    print("You Bust! Dealer wins")

elif player_total > dealer_total:
    print('You win')
    balance.win(bet1 * 2)

elif player_total < dealer_total:
    print('Dealer wins')

else:
    print('Tie')
    balance.win(bet1)

update_balance("BlackJack.txt", player_name, balance.show(), data)

print()
print(f'Current balance: ${balance.show()}')

