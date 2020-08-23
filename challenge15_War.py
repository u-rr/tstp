from random import shuffle

class Card:
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    
    values = [
            None, None,
            '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'
    ]
    
    def __init__(self, v: int, s: int):
        """スートも値も整数値です"""
        self.value: int = v
        self.suit: int = s
        
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            # if self.suit < c2.suit:
            #     return True
            # else:
            #     return False
            return self.suit < c2.suit
        return False
        
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            # if self.suit > c2.suit:
            #     return True
            # else:
            #     return False
            return self.suit > c2.suit
        return False
        
    def __repr__(self):
        v = self.values[self.value] + ' of ' \
            + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
        
    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input('プレーヤー１の名前：')
        name2 = input('プレーヤー２の名前：')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    # def wins(self, winner):
    #     w = 'このラウンドは {} が勝ちました'.format(winner)
    #     print(w)
    
    def print_winner(self, winner):
        print('このラウンドは {} が勝ちました'.format(winner.name))
    
    # def draw(self, p1n, p1c, p2n, p2c):
    #     d = '{} は {}、{} は {} を引きました'.format(p1n, p1c, p2n, p2c)
    #     print(d)
    
    def print_draw(self, p1, p2):
        print('{} は {}、{} は {} を引きました'.format(p1.name, p1.card, p2.name, p2.card))
    
    def play_game(self):
        cards = self.deck.cards
        print('戦争を始めます！')
        while len(cards) >= 2:
            response = input('q　で終了、それ以外のキーでPlay：')
            if response == 'q':
                break
            # p1c = self.deck.draw()
            self.p1.card = self.deck.draw()
            # p2c = self.deck.draw()
            self.p2.card = self.deck.draw()
            # p1n = self.p1.name
            # p2n = self.p2.name
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)
        win = self.winner(self.p1, self.p2)
        print('ゲーム終了、{}の勝利です！'.format(win))
        
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return '引き分け！'

game = Game()
game.play_game()
