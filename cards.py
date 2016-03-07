import random

CUT_ERROR = 10
SHUFFLE_START_ERROR = 4
SHUFFLE_ERROR = 1


def rand(a, b):
    return random.SystemRandom().randint(a, b)


def randBool():
    return random.SystemRandom().choice([True, False])


def standardDeck():
    standard_deck = []
    for card_num in range(2, 15):
        for suit in range(0, 4):
            standard_deck.append(Card(card_num, suit))
    return tuple(standard_deck)


def normalDist(a, b, trials):
    out = 0
    for _ in range(0, trials):
        out += rand(a, b)
    return out/trials


def shuffleAlgo(func):
    def shuff(deck):
        array = func(deck.cards)
        return Deck(cards=array)
    return shuff


class Card:
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    SPADES = 0
    HEARTS = 1
    CLUBS = 2
    DIAMONDS = 3

    def __init__(self, card_num, suit):
        if not 2 <= card_num <= 14:
            raise ValueError("Card number is invalid.")
        if not 0 <= suit <= 3:
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

        if self.suit == self.SPADES:
            suit = "♠"
        elif self.suit == self.HEARTS:
            suit = "♡"
        elif self.suit == self.CLUBS:
            suit = "♣"
        elif self.suit == self.DIAMONDS:
            suit = "♢"

        return card + suit

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


class Deck:
    def __init__(self, cards=standardDeck()):
        self.cards = list(cards)

    def realShuffle(self):
        cut = int(len(self.cards)/2 + normalDist(-CUT_ERROR, CUT_ERROR, 3))
        a = self.cards[:cut]
        b = self.cards[cut:]
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

        self.cards = temp_deck

    def randShuffle(self):
        temp_deck = self.cards[:]
        self.cards = []

        while len(temp_deck) > 0:
            self.cards.append(temp_deck.pop(rand(0, len(temp_deck)-1)))

    def deal(self):
        return self.cards.pop(0)

    def addCard(self, card):
        self.cards.append(card)

    def addCardMiddle(self, card):
        cut = int(len(self.cards)/2 + normalDist(-CUT_ERROR, CUT_ERROR, 3))
        a = self.cards[:cut]
        b = self.cards[cut:]
        self.cards = a + [card] + b

    def cutDeck(self):
        cut = int(len(self.cards)/2 + normalDist(-CUT_ERROR, CUT_ERROR, 3))
        a = self.cards[:cut]
        b = self.cards[cut:]
        self.cards = b + a

    def __str__(self):
        out = ""
        for i in self.cards:
            out += str(i) + "\n"
        return out[:-1]

    def __len__(self):
        return len(self.cards)

    def __contains__(self, item):
        return item in self.cards

    def __iter__(self):
        return iter(self.cards)

    def __eq__(self, other):
        a = self.cards[:]
        b = other.cards[:]

        if len(self) != len(other):
            return False
        for card in a:

            if card in b:
                a.remove(card)
                b.remove(card)

            else:
                return False
        return True
