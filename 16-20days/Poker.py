"""
类和类的关系：
is:继承关系，最为强烈。
    比如学生和人的关系、手机和电子产品的关系都属于继承关系
has：关联/聚合/合成关系，不好界定，很微妙。
    比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；
    如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
use:依赖关系，程度很轻。类中的某个方法的参数是另外一个类
    比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。
"""

from enum import Enum, unique      # 载入Enum枚举类型
import random

@unique                            # 限制不能定义相同值的成员
class Suit(Enum):                  # 继承关系
    """定义花色"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
    def It(self, other):
        return self.value > other.value

class Card():
    """定义牌面"""
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
    def show(self):
        suits = ['♠︎', '♥︎', '♣︎', '♦︎']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suits[self.suit]}:{faces[self.face]}'
    def __repr__(self):
        return self.show()

class Poker():
    """发牌"""
    def __init__(self):
        self.index = 0
        self.cards = [Card(suit, face) for suit in range(4) for face in range(1, 14)]    # 依赖关系
    def shuffle(self):
        random.shuffle(self.cards)
        self.index = 0
    def deal(self):
        card = self.cards[self.index]
        self.index += 1
        return card
    @property
    def has_more(self):
        return self.index < len(self.cards)

class Player():
    """定义玩家"""
    def __init__(self, name):
        self.name = name
        self.cards = []
    def get_one(self, card):
        """摸一张牌"""
        self.cards.append(card)
    def sort(self, comp = lambda card:(card.suit, card.face)):                    # 关联关系
        """整理手上的牌"""
        self.cards.sort(key=comp)
    def print_cards(self):
        """显示手上的牌"""
        print(f'{self.name}:{self.cards}')
def main():
    poker = Poker()
    poker.shuffle()
    players = [Player('111'), Player('222'), Player('333'), Player('444')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.deal())
    for player in players:
        player.sort()
        player.print_cards()

if __name__ == '__main__':
    main()