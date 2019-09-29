#!/usr/bin/env python
# coding: utf-8


def find_subarr(input_lst, num):
    '''
    Метод, находящий подмассив, сумма чисел которого равна заданному числу
    O(n) по времени
    :param input_lst: массив
    :param num: искомое число
    :return: два индекса (начала и конца подмассива). Пустой tuple, если таких нет
    Пример: find_subarr([1, 2, 3, 4, 5, -1], 4) может вернуть (3, 3) или (4, 5)
    '''
    sl = {}
    sum = 0
    for i in range(len(input_lst)):

            sum += input_lst[i]
            if sum == num:
                return (0, i)
            elif (sum - num) in sl:
                return (sl[sum - num]+1, i)
            sl[sum] = i
    return ()


input_lst = [3, 1, 1, 2, 4, 5]
num = int(input())
print(find_subarr(input_lst, num))
