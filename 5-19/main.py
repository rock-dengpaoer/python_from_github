# def gcd(x, y):
#     """求最大公约数"""
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#
#
# def lcm(x, y):
#     """求最小公倍数"""
#     return x * y // gcd(x, y)
#
#
# def is_palidrome(num):
#     """"判断一个数是不是回文数"""
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#     return total == num
#
#
# def is_prime(num):
#     """判断一个数是不是素数"""
#     for factor in range(2, int(num ** 0.5) + 1):
#         if num % factor == 0:
#             return False
#     return True if num != 1 else False
#
#
# if __name__ == '__main__':
#     num = int(input('请输入正整数：'))
#     if is_palidrome(num) and is_prime(num):
#         print('%d是回文素数'% num)
#     else:
#         print('NO')
#

# def foo():
#     b = 'hello'
#
#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)
#     bar()
#
#
# if __name__ == '__main__':
#     a = 100
#     foo()


# def foo():
#     b = 'hello'
#
#     # Python中可以在函数内部再定义函数
#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)
#
#     bar()
#     # print(c)  # NameError: name 'c' is not defined
#
#
# if __name__ == '__main__':
#     a = 100
#     # print(b)  # NameError: name 'b' is not defined
#     foo()


# def foo():
#     global a
#     a = 200
#     print(a)
#
#
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)


# def main():
#     pass
# if __name__ == '__main__':
#     main()


# s1 = 'hello,world'
# s2 = 'hello,world'
# s3 = """
# hello,
# world!
# """
# print(s1, s2, s3, end='')


# s1 = '\'hello,world!\''
# s2 = '\n\\hello,world!\\\n'
# print(s1, s2, end='')


# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1, s2)


# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')


# s1 = 'hello ' * 3
# print(s1)
# s2 = 'world'
# s1 += s2
# print(s1)
# print('ll' in s1)
# print('good' in s1)
# str2 = 'abc123456'
# print(str2[2])
# print(str2[2:5])
# print(str2[2:])
# print(str2[2::2])
# print(str2[::2])
# print(str2[::-1])
# print(str2[-3:-1])
#
#
# str1 = 'hello,world!'
# print(len(str1))
# print(str1.capitalize())
# print(str1.title())
# print(str1.upper())
# print(str1.find('or'))
# print(str1.find('shit'))
# print(str1.startswith('He'))
# print(str1.startswith('hel'))
# print(str1.endswith('!'))
# print(str1.center(50, '*'))
# print(str1.rjust(50, ' '))
# str2 = 'abc123456'
# print(str2.isdigit())

# a, b = 5, 10
# print('%d * %d = %d' % (a, b, a * b))
# print('{0} * {1} = {2}'.format(a, b, a * b))
# print(f'{a} * {b} = {a * b}')


# list1 = [1, 3, 5, 7, 100]
# print(list1)
# list2 = ['hello'] * 3
# print(list2)
# print(len(list1))
# print(list1[0])
# print(list1[4])
# print(list1[-1])
# print(list1[-3])
# list1[2] = 300
# print(list1)
# for index in range(len(list1)):
#     print(list1[index])
# for elem in list1:
#     print(elem)
# for index, elem in enumerate(list1):
#     print(index, elem)


# list1.append(200)
# list1.insert(1, 400)
# list1 += [1000, 2000]
# print(list1)
# print(len(list1))
# if 3 in list1:
#     list1.remove(3)
# print(list1)
# if 1234 in list1:
#     list1.remove(1234)
# print(list1)
# list1.pop(0)
# print(list1)
# list1.pop(len(list1)-1)
# print(list1)
# list1.clear()
# print(list1)


# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# # print(fruits)
# fruits += ['pitaya', 'peer', 'mango']
# # print(fruits)
# fruits2 = fruits[1:4]
# print(fruits2)
# fruits3 = fruits[:]
# print(fruits3)
# fruits4 = fruits[-3:-1]
# print(fruits4)
# fruits5 = fruits[::-1]
# print(fruits5)


# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# print(list2)
# print(list1)
# list3 = sorted(list1, reverse=True)
# print(list3)
# list4 = sorted(list1, key=len)
# print(list4)
# list1.sort(reverse=True)
# print(list1)
# import sys
#
# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))
# print(f)
# f = (x ** 2 for x in range(1,1000))
# print(sys.getsizeof(f))
# print(f)
# for val in f:
#     print(val)


# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
#
# def main():
#     for val in fib(20):
#         print(val)
#
#
# if __name__ == '__main__':
#     main()


# t = ('rock', 38, True, 'anhui')
# print(t)
# print(t[0])
# print(t[3])
# for member in t:
#     print(member)
# t = ('hhh', 18, True, 'beijing')
# print(t)
# person = list(t)
# print(person)
# person[0] = 'dsa'
# person[1] = 21
# print(person)
# fruits_list = ['apple', 'banana', 'orange']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)


# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
# print('length =', len(set1))
# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 2, 1))
# print(set2, set3)
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)
#
#
# set1.add(4)
# print(set1)
# set1.add(5)
# print(set1)
# print(set2)
# set2.update([11, 12])
# print(set2)
# set2.discard(5)
# print(set2)
# if 4 in set2:
#     set2.remove(4)
# print(set2)
# print(set3.pop())
# print(set3)
#
# print('set1=', end='')
# print(set1)
# print('set2=', end='')
# print(set2)
# print('set1 & set2=', end='')
# print(set1 & set2)
# print('set1 | set2=', end='')
# print(set1 | set2)
# print('set1 ^ set2=', end='')
# print(set1 ^ set2)
# print('set2 <= set1=', end='')
# print(set2 <= set1)
# print('set3 <= set1=', end='')
# print(set3 <= set1)
# print('set1 >= set2=', end='')
# print(set1 >= set2)
# print('set1 >= set3=', end='')
# print(set1 >= set3)


scores = {'rock': 21, 'hh':22, 'aa': 33}
print('scores=', end='')
print(scores)
items1 = dict(one=1, two=2, three=3, four=4)
items2 = dict(zip(['a', 'b', 'c'], '123'))
items3 = {num: num ** 2 for num in range(1, 10)}
print('items1=', end='')
print(items1)
print('items2=', end='')
print(items2)
print('items3', end='')
print(items3)
print(scores['rock'])
print(scores['hh'])
for key in scores:
    print(f'{key}:{scores[key]}')
scores['qq'] = 78
scores['oo'] = 12
scores.update(jj=13,zxc=21)
print(scores)
if 'hh' in scores:
    print(scores['hh'])
print(scores.get('hh'))
print(scores.get('hh', 60))
print(scores)
print(scores.popitem())
print(scores)
print(scores.popitem())
print(scores)
print(scores.pop('rock', 100))
print(scores)