# def douhaohanshu(numberlist, newlist=None):
#     for i in range(len(numberlist) - 1):
#         newlist.append(numberlist[i])
#         newlist.append(',')
#     newlist.append('and ')
#     newlist.append(numberlist[len(numberlist)-1])
#
#
# spam = ['apples', 'bananas', 'tofu', 'cats', 'wula']
# new = []
# douhaohanshu(spam, new)
# print(spam)
# for i in range(len(new)):
#     print(new[i], end='')
#
# grid = [
#     ['.', '.', '.', '.', '.', '.'],
#     ['.', '0', '0', '.', '.', '.'],
#     ['0', '0', '0', '0', '.', '.'],
#     ['0', '0', '0', '0', '0', '.'],
#     ['.', '0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0', '.'],
#     ['0', '0', '0', '0', '.', '.'],
#     ['.', '0', '0', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.'],
# ]
#
#
# for j in range(len(grid[1])):
#     for i in range(len(grid)):
#         print(grid[i][j], end='')
#     print()


# birthdays = {'Alice': 'Apr 1'}
#
# while True:
#     print('enter')
#     name = input()
#     if name == ' ':
#         break
#     if name in birthdays:
#         print(birthdays[name] + 'is the birthday of' + name)
#     else:
#         print('sorry')
#         print('what is their birthdays')
#         bady = input()
#         birthdays[name] = bady
#         print('over')


# prinicItems = {'apples': 5, 'cups': 2}
# print(str(prinicItems.get('ap', 0)))

# import pprint
#
# message = 'it wadsahjkhvseafnkjl.sfsda./waersdf'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# print(pprint.pformat(count))
# pprint.pprint(count)

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True


# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi i a phone number:')
# print(isPhoneNumber('Moshi moshi'))


# import re
#
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242')
# print('Phone number found:' + mo.group())
# print(mo.group(1))
# print(mo.group(0))
# print(mo.group(2))
import os.path

# import pyperclip, re
#
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?
#     (\s|-|\.)?
#     (\d{3})
#     (\s|-|\.)
#     (\d{4})
#     (\s*(ext|x|ext.)\s*(\d{2, 5}))?
# )''', re.VERBOSE)
#
# text = str(pyperclip.paste())
# matches = []
# for groups in phoneRegex.findall(text):
#     phoneNum = '-'.join([groups[1], groups[3], groups[5]])
#     if groups[8] != '':
#         phoneNum += 'x' + groups[8]
#     matches.append(phoneNum)
#
# if len(matches) > 0:
#     pyperclip.copy('\n'.join(matches))
#     print('Copied to clipboard:')
#     print('\n'.join(matches))
# else:
#     print('No phone numbers found.')

import os

# myfiles = ['adas', 'dsa']
# for filename in myfiles:
#     print(os.path.join('C:\\user', filename))

# print(os.getcwd())
# os.chdir('c:\\windows\\System32')
# print(os.getcwd())
# print(os.path.abspath('.'))
# print(os.path.abspath('.\\Scripts'))
# print(os.path.isabs('.'))
# print(os.path.isabs(os.path.abspath('.')))
# print(os.path.relpath('C:\\Windows', 'C:\\'))
# print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
# print(os.getcwd())
from functools import wraps


def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(x, y, z)


# fish = 6
# while True:
#     total = fish
#     enough = True
#     for _ in range(5):
#         if (total - 1) % 5 == 0:
#             total = (total - 1) // 5 * 4
#         else:
#             enough = False
#             break
#     if enough:
#         print(fish)
#         break
#     fish += 5


# class Thing(object):
#
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     @property
#     def value(self):
#         return self.price / self.weight
#
#
# def input_thing():
#     name_str, price_str, weight_str = input().split()
#     return name_str, int(price_str), int(weight_str)
#
#
# def main():
#     max_weight, num_of_things = map(int, input().split())
#     all_things = []
#     for _ in range(num_of_things):
#         all_things.append(Thing(*input_thing()))
#     all_things.sort(key=lambda x: x.value, reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight <= max_weight:
#             print(f'小偷拿走了{thing.name}')
#             total_weight += thing.weight
#             total_price += thing.price
#     print(f'总价值:{total_price}美元')
#
#
# if __name__ == '__main__':
#     main()


import sys
import time

SIZE = 6
total = 0


# def print_board(board):
#     for row in board:
#         for col in row:
#             print(str(col).center(4), end='')
#         print()
#
#
# def patrol(board, row, col, step=1):
#     if 0 <= row < SIZE and \
#             0 <= col < SIZE and \
#             board[row][col] == 0:
#         board[row][col] = step
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f'第{total}种走法：')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col] = 0
#
#
# def main():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     patrol(board, SIZE - 1, SIZE - 1)
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     items = list(map(int, input().split()))
#     overall = partial = items[0]
#     for i in range(1, len(items)):
#         partial = max(items[i], partial + items[i])
#         overall = max(partial, overall)
#     print(overall)
#
#
# def record_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         print(f'{func.__name__}:{time() - start}秒')
#         return result
#     return wrapper
#
#
# if __name__ == '__main__':
#     main()

# def singleton(cls):
#     instances = {}
#
#     @wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrapper
#
#
# @singleton
# class President:
#     pass


from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory:

    @staticmethod
    def create(emp_type, *args, **kwargs):
        all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
        cls = all_emp_types[emp_type.upper()]
        return cls(*args, **kwargs) if cls else None


def main():
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}: {emp.get_salary():.2f}元')


if __name__ == '__main__':
    main()