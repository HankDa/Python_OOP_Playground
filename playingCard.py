from abc import ABCMeta
from abc import abstractclassmethod

class Card(metaclass=ABCMeta):
    @abstractclassmethod
    def card_value_numeric(self):
        raise NotImplementedError()
    @abstractclassmethod
    def card_suit(self):
        raise NotImplementedError()
    def __lt__(self, other):
        return self.card_value_numeric < other.card_value_numeric
    
class PlayingCard(Card):
    suits = {"Spades","Diamonds","Hearts","Clubs"}
    # TODO: what is ** for?? -> unpack dictionary 
    values = {
        "A": 1,
        **{str(i): i for i in range(2, 11)},
        "J": 11,
        "Q": 12,
        "K": 13,
    }
    def __init__(self,suit,val) -> None:
        super().__init__()
        if suit in PlayingCard.suits:
            self._suit = suit
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
    values = {"Red":14,"Black":14}
    suits = {"Joker"}

    def __init__(self, suit, val) -> None:
        super().__init__()
        if suit in Joker_card.suits:
            self._suit = suit
        else:
            raise ValueError("Please choose the suits from: {}".format(", ".join(Joker_card.suits)))
        if val in Joker_card.values:
            self._value = val
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

class Hand:
    def __init__(self,cards:list[Card]) -> None:
        # unpack cards and store it into list
        self._cards= cards
    @property
    def cards(self):
        return self._cards
    def show_cards(self):
        return ",".join([card.display_card() for card in self.cards])
    def __lt__(self, other):
        # TODO: check this code: zip/ sorted(object)/reversed -> done
        # - The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
        for card_a, card_b in zip(sorted(self.cards, key= lambda card: card.card_value_numeric, reverse= True), sorted(other.cards,key= lambda card: card.card_value_numeric, reverse= True)):
            if card_a < card_b:
                return True
            elif card_b < card_a:
                return False
        return False
    

class Game:
    def __init__(self):
        # The colon here is a annotation indicated the which is a list of card object
        self._cards: list[Card] = []
        self._hands: list[Hand] = []
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
    @property
    def hands(self):
        return self._hands
    def add_hand(self, card_indices: list[int]) -> None:
        self.hands.append(Hand([self.cards[i] for i in card_indices]))

    def hand_string(self, hand: int) -> str:
        return self.hands[hand].show_cards()
    
    def hand_beats(self, hand_a: int, hand_b: int) -> bool:
        return self.hands[hand_a] > self.hands[hand_b]



if __name__ == '__main__':
    game = Game()
    hand_a_list = []
    print("please enter the amount of cards:")
    n_1 = int(input())
    for i in range(n_1):
      print("please enter the information of the card:")
      suit, value = input().split()
      game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
      hand_a_list.append(i)
    game.add_hand(hand_a_list)
    print(game.hand_string(0))
    hand_b_list = []
    n_2 = int(input())
    for i in range(n_1, n_1 + n_2):
      print("please enter the information of the card:")
      suit, value = input().split()
      game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
      hand_b_list.append(i)
    game.add_hand(hand_b_list)
    print(game.hand_string(1))
    print("true" if game.hand_beats(0, 1) else "false")

    
