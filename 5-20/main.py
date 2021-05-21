# import os
# import time
#
#
# def main():
#     content = 'abcdef'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
#
# if __name__ == '__main__':
#     main()


# import random
#
#
# def generate_code(code_len=4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code
#
#
# def get_suffix(filename, has_dot=False):
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index]
#     else:
#         return ''


# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2


# def is_leap_year(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# def which_day(year, month, date):
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date


# def yanhui():
#     num = int(input('NUmber of rows: '))
#     yh = [[]] * num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()


# from random import randint, sample
#
#
# def display(balls):
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end='')
#         print('%02d' % ball, end=' ')
#     print()


# def random_select():
#     red_balls = [x for x in range(1, 34)]
#     select_balls = []
#     select_balls = sample(red_balls, 6)
#     select_balls.sort()
#     select_balls.append(randint(1, 16))
#     return select_balls


# def shuanseqiu():
#     n = int(input('机选几注： '))
#     for _ in range(n):
#         display(random_select())


# def yuesefu():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#         if number == 9:
#             persons[index] = False
#             counter += 1
#             number = 0
#         index += 1
#         index %= 30
#     for person in persons:
#         print('基' if person else '非', end='')


# import os
#
#
# def print_board(board):
#     print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
#     print('-+-+-')
#     print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
#     print('-+-+-')
#     print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])
#
#
# def jing():
#     init_board = {
#         'TL': ' ', 'TM': ' ', 'TR': ' ',
#         'ML': ' ', 'MM': ' ', 'MR': ' ',
#         'BL': ' ', 'BM': ' ', 'BR': ' '
#     }
#     begin = True
#     while begin:
#         curr_board = init_board.copy()
#         begin = False
#         turn = 'x'
#         counter = 0
#         os.system('clear')
#         print_board(curr_board)
#         while counter < 9:
#             move = input('轮到%s走棋，请输入位置：' % turn)
#             if curr_board[move] == ' ':
#                 counter += 1
#                 curr_board[move] = turn
#                 if turn == 'x':
#                     turn = 'o'
#                 else:
#                     turn = 'x'
#             os.system('clear')
#             print_board(curr_board)
#             choice = input('再玩一局？（yes|no）')
#             begin = choice == 'yes'
#
#
# if __name__ == '__main__':
#     # yanhui()
#     # shuanseqiu()
#     # yuesefu()
#     jing()

# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def study(self, course_name):
#         print('%s正在学习%s.' % (self.name, course_name))
#
#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》.' % self.name)
#         else:
#             print('%s can watch japan.' % self.name)
#
#
# def class_1():
#     stu1 = Student('das', 12)
#     stu1.study('c++')
#     stu1.watch_movie()
#     stu2 = Student('csda', 32)
#     stu2.study('java')
#     stu2.watch_movie()
#
#
# class Test:
#     def __init__(self, foo):
#         self.__foo = foo
#
#     def __bar(self):
#         print(self.__foo)
#         print('__bar')
#
#
# def test_test():
#     test = Test('hello')
#     test._Test__bar()
#     print(test._Test__foo)
#
#
# if __name__ == '__main__':
#     # class_1()
#     test_test()


# from time import sleep
#
#
# class Clock(object):
#
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def run(self):
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)
#
#
# def clock():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
#
# if __name__ == '__main__':
#     clock()


from math import sqrt


# class Point(object):
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def move_to(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move_by(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#     def distrance_to(self, other):
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
#
#     def __str__(self):
#         return '(%s, %s)' % (str(self.x), str(self.y))


# def main():
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     p2.move_by(-1, 2)
#     print(p2)
#     print(p1.distrance_to(p2))


# class Person(object):
#
#     __slots__ = ('_name', '_age', '_gender')
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('%s在飞行棋' % self._name)
#         else:
#             print('%s斗地主' % self._name)


# from math import sqrt
#
#
# class Triangle(object):
#
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def is_valid(a, b, c):  # 判断能否构成三角形
#         return a + b > c and b + c > a and a + c > b
#
#     def perimeter(self):
#         return self._a + self._b + self._c
#
#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


from time import time, localtime, sleep


# class Clock(object):
#
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
#
#     def run(self):
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


# class Person(object):
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         print('%s正在快乐的玩耍' % self._name)
#
#     def watch_av(self):
#         if self._age >= 18:
#             print('%s正在观看爱情动作片' % self._name)
#         else:
#             print('%s只能看熊出没' % self._name)


# class Student(Person):
#
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade
#
#     @property
#     def grade(self):
#         return self._grade
#
#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
#
#     def study(self, course):
#         print('%s的%s正在学习%s' % (self._grade, self._name, course))


# class Teacher(Person):
#
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title
#
#     @property
#     def title(self):
#         return self._title
#
#     @title.setter
#     def title(self, title):
#         self._title = title
#
#     def teach(self, course):
#         print('%s%s正在讲%s' % (self._name, self._title, course))


# from abc import ABCMeta, abstractmethod

# class Pet(object, metaclass=ABCMeta):
#
#     def __init__(self, nickname):
#         self._nickname = nickname
#
#     @abstractmethod
#     def make_voice(self):
#         pass

# class Dog(Pet):
#
#     def make_voice(self):
#         print('%s:汪汪汪·····' % self._nickname)

# class Cat(Pet):
#
#     def make_voice(self):
#         print('%s:喵喵喵。。。' % self._nickname)


# def main():
    # person = Person('rock', 12)
    # person.play()
    # person.age = 22
    # person.play()
    # person._gender = '男'
    # a, b, c = 3, 4, 5
    # if Triangle.is_valid(a, b, c):
    #     t = Triangle(a, b, c)
    #     print(t.perimeter())  # 周长
    #     print(t.area())  # 面积
    # else:
    #     print('无法构成三角形')
    # clock = Clock.now()
    # while True:
    #     print(clock.show())
    #     sleep(1)
    #     clock.run()
    # stu = Student('dsa', 12, '大一')
    # stu.study('高数')
    # stu.watch_av()
    # t = Teacher('qwe', 66, '教授')
    # t.teach('c++')
    # t.watch_av()
    # pets = [Dog('旺财'), Cat('克缇'), Dog('大黄')]
    # for pet in pets:
    #     pet.make_voice()


# if __name__ == '__main__':
#     main()
