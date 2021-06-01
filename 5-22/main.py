# # def main():
# #     f = None
# #     try:
# #         with open('致橡树.txt', 'r', encoding='utf-8') as f:
# #             print(f.read())
# #     except FileNotFoundError:
# #         print('无法打开指定的文件')
# #     except LookupError:
# #         print('指定了未知的编码')
# #     except UnicodeDecodeError:
# #         print('读取文件时解码错误')
# #     finally:
# #         if f:
# #             f.close()
# #
# #
# # if __name__ == '__main__':
# #     main()
#
#
# # import time
# # #
# # #
# # # def main():
# # #     print('一次性读取整个文件')
# # #     with open('test.txt', 'r', encoding='utf-8') as f:
# # #         print(f.read())
# # #     print('for-in循环逐行读取')
# # #     with open('test.txt', mode='r') as f:
# # #         for line in f:
# # #             print(line, end='')
# # #             time.sleep(0.5)
# # #     print()
# # #     print('读取文件按行读取到列表中')
# # #     with open('test.txt') as f:
# # #         lines = f.readlines()
# # #     print(lines)
#
#
# from math import sqrt
# import json
# import re
#
#
# def is_prime(n):
#     assert n > 0
#     for factor in range(2, int(sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False
#
#
# def main():
#     # filenames = ('a.txt', 'b.txt', 'c.txt')
#     # fs_list = []
#     # try:
#     #     for filename in filenames:
#     #         fs_list.append(open(filename, 'w', encoding='utf-8'))
#     #     for number in range(1, 10000):
#     #         if is_prime(number):
#     #             if number < 100:
#     #                 fs_list[0].write(str(number) + '\n')
#     #             elif number < 10000:
#     #                 fs_list[1].write(str(number) + '\n')
#     #             else:
#     #                 fs_list[2].write(str(number) + '\n')
#     # except IOError as ex:
#     #     print(ex)
#     #     print('写文件时发生错误')
#     # finally:
#     #     for fs in fs_list:
#     #         fs.close()
#     # print('操作完成')
#
#     # try:
#     #     with open('logo.png', 'rb') as fs1:
#     #         data = fs1.read()
#     #         print(type(data))
#     #     with open('copy.png', 'wb') as fs2:
#     #         fs2.write(data)
#     # except FileNotFoundError as e:
#     #     print('指定的文件打不开')
#     # except IOError as e:
#     #     print('读写文件时出现错误')
#     # print('程序执行结束')
#     # mydict = {
#     #     "name": "rock",
#     #     "age": 12,
#     #     "qq": 123456789,
#     #     "friend": ["asd", "ds", "cx"],
#     #     "cars":[
#     #         {"brand": "BYD", "max_speed": 180},
#     #         {"brand": "Audi", "max_speed": 280}
#     #     ]
#     # }
#     # mydict2 = {
#     #     "name": "rock-2",
#     #     "age": 12,
#     #     "qq": 123456789,
#     #     "friend": ["asd", "ds", "cx"],
#     #     "cars": [
#     #         {"brand": "BYD", "max_speed": 180},
#     #         {"brand": "Audi", "max_speed": 280}
#     #     ]
#     # }
#     # try:
#     #     with open('data.json', 'w', encoding='utf-8') as fs:
#     #         json.dump(mydict, fs)
#     #         json.dump(mydict2, fs)
#     # except IOError as e:
#     #     print(e)
#     # print('over')
#
#
#     username = input('请输入用户名：')
#     qq = input('请输入QQ号')
#     m1 = re.match(r'^[0-9a-zA-Z_]{6, 20}$', username)
#     if not m1:
#         print('请输入有效的用户名')
#     m2 = re.match(r'^[1-9]\d{4,11}$', qq)
#     if not m2:
#         print('请输入有效的QQ号')
#     if m1 and m2:
#         print('你输入的信息是有效的')
#
#
# if __name__ == '__main__':
#     main()

#
# from random import randint
# from time import time, sleep
# from multiprocessing import Process
# from os import getpid
# from threading import Thread
#
#
# def download_task(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成!耗费了%d秒' % (filename, time_to_download))
#
#
# class DownloadTask(Thread):
#
#     def __init__(self, filename):
#         super().__init__()
#         self._filename = filename
#
#     def run(self):
#         print('开始下载%s...' % self._filename)
#         time_to_download = randint(5, 10)
#         sleep(time_to_download)
#         print('%s下载完成!耗费了%d秒' % (self._filename, time_to_download))
#
#
# def main():
#     start = time()
#     # download_task('python从入门到放弃.pdf')
#     # download_task('peking Hot.avi')
#     # end = time()
#     # p1 = Thread(target=download_task, args=('pyhton从入门到放弃.pdf', ))
#     # p1.start()
#     # p2 = Thread(target=download_task, args=('peking Hot.avi',))
#     # p2.start()
#     # p1.join()
#     # p2.join()
#     t1 = DownloadTask('pyhton从入门到放弃.pdf')
#     t1.start()
#     t2 = DownloadTask('peking Hot.avi')
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.2f秒' % (end - start))
#
#
# if __name__ == '__main__':
#     main()


from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 2)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为：￥%d元' % account.balance)


# if __name__ == '__main__':
#     main()