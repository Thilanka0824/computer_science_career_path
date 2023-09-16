import random 

class Player:
    def __init__(self, score):
        self.score = score
    
    


class Cards:
    deck = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    @classmethod
    def shuffle(cls):
        # shuffle the deck
        random.shuffle(cls.deck)

    @classmethod
    def deal(cls):
        # deal a card from the top of the deck
        card = cls.deck.pop(0)
        suit = cls.suits[random.randint(0, 3)]
        return cls(suit, card)


player_1 = Player(0)
hand = Cards.deal()

print(hand)