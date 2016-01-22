import random

CUT_ERROR = 10
SHUFFLE_START_ERROR = 4
SHUFFLE_ERROR = 1


def rand(a,b):
    return random.SystemRandom().randint(a,b)

def randBool():
    return random.SystemRandom().choice([True,False])

class Card:
    jack = 11
    queen = 12
    king = 13
    ace = 14

    spades = 0
    hearts = 1
    clubs = 2
    diamonds = 3


    def __init__(self, card_num, suite):
        assert card_num in range(0,15)
        assert suite in range(0,5)
        self.card_num = card_num
        self.suite = suite

    def __str__(self):
        if self.card_num == self.jack:
            card = "Jack"
        elif self.card_num == self.queen:
            card = "Queen"
        elif self.card_num == self.king:
            card = "King"
        elif self.card_num == self.ace:
            card = "Ace"
        else:
            card = str(self.card_num)

        if self.suite == self.spades:
            suite = "Spades"
        elif self.suite == self.hearts:
            suite = "Hearts"
        elif self.suite == self.clubs:
            suite = "Clubs"
        elif self.suite == self.diamonds:
            suite = "Diamonds"

        return card + " of " + suite

    def __eq__(self, other):
        return self.card_num == other.card_num and self.suite == other.suite

    def __lt__(self, other):
        return self.card_num < other.card_num

    def __le__(self, other):
        return self.card_num <= other.card_num

    def __gt__(self, other):
        return self.card_num > other.card_num

    def __ge__(self, other):
        return self.card_num >= other.card_num


def standardDeck():
    standard_deck = []
    for card_num in range(2,15):
        for suite in range(0,4):
            standard_deck.append(Card(card_num, suite))
    return standard_deck


class Deck:
    def __init__(self,cards=standardDeck()):
        self.cards = cards

    def realShuffle(self):
        cut = int(len(self.cards)/2 + (rand(-CUT_ERROR,CUT_ERROR) + rand(-CUT_ERROR,CUT_ERROR) + rand(-CUT_ERROR,CUT_ERROR))/3)
        a = self.cards[:cut]
        b = self.cards[cut:]
        temp_deck = []

        use_a = randBool()
        cutoff = rand(0,SHUFFLE_START_ERROR)

        if use_a:
            temp_deck = a[-cutoff:] + temp_deck
            del a[-cutoff:]
        else:
            temp_deck = b[-cutoff:] + temp_deck
            del b[-cutoff:]

        while len(a)>0 or len(b)>0:
            use_a = not use_a
            shuffle_error = rand(0,SHUFFLE_ERROR) + 1
            if use_a:
                if(len(a)>0):
                    temp_deck = a[-shuffle_error:] + temp_deck
                    del a[-shuffle_error:]
            else:
                if(len(b)>0):
                    temp_deck = b[-shuffle_error:] + temp_deck
                    del b[-shuffle_error:]
        self.cards = temp_deck

    def randShuffle(self):
        temp_deck = self.cards
        del self.cards
        self.cards = []
        while len(temp_deck) > 0:
            self.cards.append(temp_deck.pop(rand(0,len(temp_deck)-1)))

    def deal():
        return self.cards.pop(0)

    def __str__(self):
        out = ""
        for i in self.cards: out+= str(i) + "\n"
        return out

    def __len__(self):
        return len(self.cards)
