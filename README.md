## about
cards is python 3 module that simulates a deck of cards. It's main feature is `Deck.realShuffle()` which attempts to simulate human shuffling. It is available under the MIT License.

## usage
````python
from cards import Deck, Card

deck = Deck() #creates a new standard Deck
#or
deck = Deck(cards=array_of_cards) #creates a deck from a Card array

deck.realShuffle() #shuffles realisticaly
#or
deck.randShuffle() #shuffles randomly

card = deck.deal() #returns the top card and removes it
````

## realShuffle()
realshuffle() tries to simulate a [riffle shuffle](https://en.wikipedia.org/wiki/Shuffling#Riffle)

realShuffle() uses 3 constants:
````python
CUT_ERROR = 10
SHUFFLE_START_ERROR = 4
SHUFFLE_ERROR = 1
````
`CUT_ERROR`: this is how far from the middle the deck it cut. 3 ±randoms are averaged for the used result.

`SHUFFLE_START_ERROR`: this is how many cards can be dropped initially. it is a random range.

`SHUFFLE_ERROR`: this is how many cards are dropped each time. a random between 1 and `SHUFFLE_ERROR`+1.