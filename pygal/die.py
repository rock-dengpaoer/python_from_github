from random import randint

class Die:

    def __init__(self, num_sides=6):
        self.num_side = num_sides

    def roll(self):
        # 返回一个位于1和骰子函数之间的随机值
        return randint(1, self.num_side)
