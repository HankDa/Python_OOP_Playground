from abc import ABCMeta
from abc import abstractclassmethod

class Card(metaclass=ABCMeta):
    @abstractclassmethod
    def card_value(self):
        raise NotImplementedError()
    @abstractclassmethod
    def card_suit(self):
        raise NotImplementedError()
    
class PlayingCard(Card):
    suits = {"spades","diamonds","hearts","clubs"}
    values = {
        "A": 1,
        **{str(i): i for i in range(2, 11)},
        "J": 11,
        "Q": 12,
        "K": 13,
    }
    def __init__(self,suit,val) -> None:
        super().__init__()
        if suit.lower() in PlayingCard.suits:
            self._suit = suit.lower()
        else:
            raise ValueError("Please choose the suits from: {}".format(", ".join(PlayingCard.suits)))
        if val in PlayingCard.values:
            self._value = val
        else:
            raise ValueError("Please choose the value from: {}".format(", ".join(PlayingCard.values.keys())))
    @property
    def card_value(self):
        return self._value
    @property
    def card_value_numeric(self):
        return PlayingCard.values[self.card_value]
    @property
    def card_suit(self):
        return self._suit
    
    def display_card(self):
        return f"{self.card_value} of {self.card_suit}"
    
class Joker_card(Card):
    values = {"red":14,"black":14}
    suits = {"joker"}

    def __init__(self, suit, val) -> None:
        super().__init__()
        if suit.lower() in Joker_card.suits:
            self._suit = suit.lower()
        else:
            raise ValueError("Please choose the suits from: {}".format(", ".join(Joker_card.suits)))
        if val.lower() in Joker_card.values:
            self._value = val.lower()
        else:
            raise ValueError("Please choose the value from: {}".format(", ".join(Joker_card.values)))   
    @property
    def card_value(self):
        return self._value
    @property
    def card_value_numeric(self):
        return Joker_card.values[self.card_value]
    @property
    def card_suit(self):
        return self._suit
    
    def display_card(self):
        return f"{self.card_value} of {self.card_suit}"

class Game:
    def __init__(self):
        # The colon here is a annotation indicated the which is a list of card object
        self._cards: list[Card] = []
    @property
    def cards(self):
        return self._cards
    def add_card(self, suit: str, value: str) -> None:
        self._cards.append(PlayingCard(suit, value))

    def card_string(self, card: int) -> str:
        return self.cards[card].display_card()

    def card_beats(self, card_a: Card, card_b: Card) -> bool:
        return self.cards[card_a].card_value_numeric > self.cards[card_b].card_value_numeric
    
    def add_joker(self, color: str) -> None:
        self._cards.append(Joker_card(suit, value))

if __name__ == '__main__':
    game = Game()
    suit, value = "Spades 6".split()
    game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
    print(game.card_string(0))
    suit, value = "Joker Red".split()
    game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")