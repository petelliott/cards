import random

CUT_ERROR = 10
SHUFFLE_START_ERROR = 4
SHUFFLE_ERROR = 1


def rand(a, b):
    return random.SystemRandom().randint(a, b)


def randBool():
    return random.SystemRandom().choice([True, False])


def standardDeck():
    suits = ("♠", "♡", "♣", "♢")
    standard_deck = []
    for card_num in range(2, 15):
        for suit in range(0, 4):
            standard_deck.append(Card(card_num, suits[suit]))
    return tuple(standard_deck)


def normalDist(a, b, trials):
    out = 0
    for _ in range(0, trials):
        out += rand(a, b)
    return out // trials


class Card:
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    SPADES = "♠"
    HEARTS = "♡"
    CLUBS = "♣"
    DIAMONDS = "♢"

    def __init__(self, card_num, suit):
        if not 2 <= card_num <= 14:
            raise ValueError("Card number is invalid.")
        if suit not in ("♠", "♡", "♣", "♢"):
            raise ValueError("Suit is invalid.")

        self.card_num = card_num
        self.suit = suit

    def __str__(self):
        if self.card_num == self.JACK:
            card = "J"
        elif self.card_num == self.QUEEN:
            card = "Q"
        elif self.card_num == self.KING:
            card = "K"
        elif self.card_num == self.ACE:
            card = "A"
        else:
            card = str(self.card_num)

        return card + self.suit

    def __eq__(self, other):
        return self.card_num == other.card_num and self.suit == other.suit

    def __lt__(self, other):
        return self.card_num < other.card_num

    def __le__(self, other):
        return self.card_num <= other.card_num

    def __gt__(self, other):
        return self.card_num > other.card_num

    def __ge__(self, other):
        return self.card_num >= other.card_num


class Deck(list):
    def __init__(self, cards=standardDeck()):
        super().__init__()
        self += list(cards)

    def realShuffle(self):
        cut = len(self)//2 + normalDist(-CUT_ERROR, CUT_ERROR, 3)
        a = self[:cut]
        b = self[cut:]
        temp_deck = []

        use_a = randBool()
        cutoff = rand(0, SHUFFLE_START_ERROR)

        if use_a:
            temp_deck = a[-cutoff:] + temp_deck
            del a[-cutoff:]
        else:
            temp_deck = b[-cutoff:] + temp_deck
            del b[-cutoff:]

        while len(a) > 0 or len(b) > 0:
            use_a = not use_a
            shuffle_error = rand(0, SHUFFLE_ERROR) + 1
            if use_a:
                if len(a) > 0:
                    temp_deck = a[-shuffle_error:] + temp_deck
                    del a[-shuffle_error:]
            else:
                if len(b) > 0:
                    temp_deck = b[-shuffle_error:] + temp_deck
                    del b[-shuffle_error:]

        del self[:]
        self += temp_deck

    def randShuffle(self):
        temp_deck = self[:]
        del self[:]

        while len(temp_deck) > 0:
            self += [temp_deck.pop(rand(0, len(temp_deck)-1))]

    def deal(self):
        return self.pop(0)

    def addCardMiddle(self, card):
        cut = len(self)//2 + normalDist(-CUT_ERROR, CUT_ERROR, 3)
        new_deck = self[:cut] + [card] + self[cut:]
        del self[:]
        self += new_deck

    def cut(self):
        cut = len(self)//2 + normalDist(-CUT_ERROR, CUT_ERROR, 3)
        new_deck = self[cut:] + self[:cut]
        del self[:]
        self += new_deck

    def __str__(self):
        out = ""
        for i in self:
            out += str(i) + "\n"
        return out[:-1]

    def __eq__(self, other):
        a = self[:]
        b = other[:]

        if len(self) != len(other):
            return False

        for card in a:
            if card in b:
                a.remove(card)
                b.remove(card)
            else:
                return False

        return True
