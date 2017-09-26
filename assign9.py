class PlayingCard:

    def __init__(self, deck, suit):               
        self.decks = {0: "Ace", 1: "Two", 2: "Three", 3: "Four", 4: "Five",
                      5: "Six", 6: "Seven", 7: "Eight", 8: "Nine", 9: "Ten",
                      10: "Jack", 11: "Queen", 12: "King"}

        
        self.suits = {'d': "Diamonds", 'c': "Clubs", 'h': "Hearts", 's': "Spades"}
        self.deck_value = deck
        self.suit_value = suit

    def getDeck(self):
        return self.decks[self.deck_value]

    def getSuit(self):      
        return self.suits[self.suit_value]

    def bjValue(self):    
        if self.deck_value == 0:
            return 1
        elif 10 <= self.deck_value <= 12:
            return 10
        else:
            return self.deck_value

    def __str__(self):
        _str = self.getDeck() + " of " + self.getSuit()
        return _str


if __name__ == "__main__":
 
    card1 = PlayingCard(7, 'd')
    print(card1)

    card2 = PlayingCard(7, 'c')
    print(card2)

    card3 = PlayingCard(7, 'h')
    print(card3)

    card4 = PlayingCard(7, 's')
    print(card4)

    card5 = PlayingCard(5, 'c')
    print(card5)
