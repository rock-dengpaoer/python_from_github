from time import time
from multiprocessing import Process, Queue
from random import randint


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    # total = 0
    # numbers_list = [x for x in range(1, 74000001)]
    # stat = time()
    # for number in numbers_list:
    #     total += number
    # print(total)
    # end = time()
    # print('time:%.3fs' % (end - stat))
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index:index+12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    start = time()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('time is :', (end - start), 's', sep='')


if __name__ == '__main__':
    main()