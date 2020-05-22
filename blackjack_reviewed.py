from random import shuffle
from os import system


def clear():
    system('clear')


ranks = ('2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', 'K ', 'A ')

suits = ('♠', '♦', '♥', '♣')

values = {'2 ': 2, '3 ': 3, '4 ': 4, '5 ': 5, '6 ': 6, '7 ': 7,
          '8 ': 8, '9 ': 9, '10': 10, 'J ': 10, 'Q ': 10, 'K ': 10, 'A ': 11}


class Card:
    '''
    Class for creating cards with rank and suit attribute
    '''

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:
    '''
    Class for creating an empty deck
    '''

    def __init__(self):
        self.deck = []

    def __str__(self):
        whole_deck = ''
        for card in self.deck:
            whole_deck += ', ' + card.__str__()
        return whole_deck

    def __len__(self):
        return len(self.deck)

    def add_card(self, card):
        self.deck.append(card)

    def shuffle(self):
        shuffle(self.deck)

    def deal_card(self):
        dealt_card = self.deck.pop()
        return dealt_card


def create_cards():
    for suit in suits:
        for rank in ranks:
            # Create cards with all possible combinations between ranks and suits
            card = Card(rank, suit)
            deck.add_card(card)  # Add the created card to the deck


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, dealt_card):
        self.cards.append(dealt_card)
        self.value += values[dealt_card.rank]
        if dealt_card.rank == 'A ':
            self.aces += 1


class Chips:
    def __init__(self, pot=0, balance=500):
        self.balance = balance
        self.pot = pot

    def place_bet(self, amount):
        self.pot += amount*2
        self.balance -= amount

    def win(self):
        self.balance += self.pot
        self.pot = 0

    def loose(self):
        self.pot = 0


def take_bet():
    print(f'You have {chips.balance}฿\n')
    while True:
        try:
            bet = int(input('\nPlace your bet, computer will bet the same amount: '))

        except BaseException:
            clear()
            print('\n'*21)
            print(f'Please enter a valid amount')

        else:
            if bet > chips.balance:
                clear()
                print('\n'*21)
                print(f'Not enough chips. You have {chips.balance}฿')
            else:
                chips.place_bet(bet)
                break


def deal_card(player):
    player.add_card(deck.deal_card())


def cards_value(player):
    if player.value <= 21:
        return player.value
    elif player.aces > 0:
        adjusted_sum = player.value
        for i in range(player.aces):
            adjusted_sum -= 10
            if adjusted_sum <= 21:
                return adjusted_sum
        return adjusted_sum
    else:
        return player.value


# new print method
def print_some_cards(player, dealer):
    print('Dealer cards')
    print_lines = [['┌───────┐'], ['│       │'], ['│       │'], ['│       │'], ['│       │'], ['│       │'],  ['└───────┘']]
    for card in dealer.cards[1:]:
        print_lines[0].append('┌───────┐')
        print_lines[1].append(f'│{card.rank}     │')
        print_lines[2].append('│       │')
        print_lines[3].append(f'│   {card.suit}   │')
        print_lines[4].append('│       │')
        print_lines[5].append(f'│     {card.rank}│')
        print_lines[6].append('└───────┘')

    for line in print_lines:
        print(''.join(line))

    print('\n')
    print_lines = [[] for list in range(7)]
    print(f'Player cards, total value: {cards_value(human_hand)}')
    for card in player.cards:
        print_lines[0].append('┌───────┐')
        print_lines[1].append(f'│{card.rank}     │')
        print_lines[2].append('│       │')
        print_lines[3].append(f'│   {card.suit}   │')
        print_lines[4].append('│       │')
        print_lines[5].append(f'│     {card.rank}│')
        print_lines[6].append('└───────┘')

    for line in print_lines:
        print(''.join(line))


def print_all_cards(player, dealer):
    print(f'Dealer cards, total value: {cards_value(computer_hand)}')
    print_lines = [[] for list in range(7)]
    for card in dealer.cards:
        print_lines[0].append('┌───────┐')
        print_lines[1].append(f'│{card.rank}     │')
        print_lines[2].append('│       │')
        print_lines[3].append(f'│   {card.suit}   │')
        print_lines[4].append('│       │')
        print_lines[5].append(f'│     {card.rank}│')
        print_lines[6].append('└───────┘')

    for line in print_lines:
        print(''.join(line))

    print('\n')
    print_lines = [[] for list in range(7)]
    print(f'Player cards, total value: {cards_value(human_hand)}')
    for card in player.cards:
        print_lines[0].append('┌───────┐')
        print_lines[1].append(f'│{card.rank}     │')
        print_lines[2].append('│       │')
        print_lines[3].append(f'│   {card.suit}   │')
        print_lines[4].append('│       │')
        print_lines[5].append(f'│     {card.rank}│')
        print_lines[6].append('└───────┘')

    for line in print_lines:
        print(''.join(line))


def bust():
    print(f'\nValue: {human_hand.value-10*human_hand.aces} BUST!\n')


def player_wins():
    if cards_value(human_hand) <= 21 and cards_value(computer_hand) <= 21 and cards_value(human_hand) > cards_value(computer_hand):
        print('\n'+'░'*39)
        print('░░░░ Player wins and takes the pot! ░░░')
        print('░'*39)
        chips.win()


def player_busts():
    if cards_value(human_hand) > 21:
        print('\n'+'░'*45)
        print('░░░░ Player busted. Dealer takes the pot ░░░░')
        print('░'*45)
        chips.loose()


def player_loose():
    if cards_value(human_hand) <= 21 and cards_value(computer_hand) <= 21 and cards_value(human_hand) < cards_value(computer_hand):
        print('\n'+'░'*38)
        print('░░░░Dealer wins and takes the pot ░░░░')
        print('░'*38)
        chips.loose()


def computer_busts():
    if cards_value(computer_hand) > 21:
        print('\n'+'░'*45)
        print('░░░░ Dealer busted. Player takes the pot ░░░░')
        print('░'*45)
        chips.win()


def push():
    if cards_value(computer_hand) == cards_value(human_hand):
        print('\n'+'░'*49)
        print('░░░░ Push, dealer and player have same value ░░░░')
        print('░'*49)


chips = Chips()

play = True
game_on = True


while play:
    clear()
    print('░'*79)
    print('░'*27 + 'Welcome to blackjack game' + '░'*27)
    print('░'*79)
    print('\n'*15)
    deck = Deck()  # Instantiating the deck
    create_cards()
    deck.shuffle()
    take_bet()
    human_hand = Hand()
    computer_hand = Hand()

    deal_card(human_hand)
    deal_card(human_hand)
    deal_card(computer_hand)
    deal_card(computer_hand)
    while game_on:
        clear()
        print_some_cards(human_hand, computer_hand)
        print('\n'*2)
        print(f'You have {chips.balance}฿ |', end=' ')
        print(f'Current pot is: {chips.pot}฿')
        option = input('\nHit or Stay (H/S):').upper()
        if option == 'H':
            deal_card(human_hand)
        elif option == 'S':
            clear()
            break
        if cards_value(human_hand) > 21:
            break

    if cards_value(human_hand) <= 21:
        while cards_value(computer_hand) < 17:
            deal_card(computer_hand)
            if cards_value(computer_hand) > 21:
                break

    clear()
    print_all_cards(human_hand, computer_hand)
    print(f'You have {chips.balance}฿ |', end=' ')
    print(f'Current pot is: {chips.pot}฿')
    player_wins()
    player_loose()
    computer_busts()
    player_busts()
    push()

    if chips.balance == 0 and chips.pot == 0:
        print('\n\n\nYou are out of ฿, go and buy some more :-(')
        break

    play_again = input('Play again ?(Y/N):').upper()
    if play_again == 'N':
        break
