import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def cardName(self):
        specialCards = {11: "Jack", 12: "Queen", 13:"King", 1: "Ace"}
        rank_name = specialCards[self.rank] if self.rank in specialCards else self.rank
        return '%s of %s'%(rank_name, self.suit)

    def show(self):
        print("{} of {}".format(self.rank, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        for suit in suits:
            for rank in range (1,14):
                self.cards.append(Card(suit,rank))
    
    def shuffle(self):
        for i in range (len(self.cards) -1, 0,-1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r], self.cards[i]       

    def drawCard(self):
        for c in self.cards:
            c.show()

    def show(self):
        for c in self.cards:
            c.show()

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance



#suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
#cards = [Card(suit, rank) for rank in range(1,14) for suit in suits]

#print(cards[1].cardName())
#cards[12].show()

myDeck = Deck()
myDeck.shuffle()
myDeck.show()