# coding=utf-8
import sys

# str = input()
# print(str)
print('Hello,World!')


def sort_method(arg):
    if not arg:
        return []
    neg = []
    pos = []
    for i in arg:
        if i < 0:
            neg.append(i)
        if i > 0:
            pos.append(i)
    result = []

    if len(pos) == 0:
        return neg

    for index in range(len(pos)):
        result.append(pos[index])
        if index < len(neg):
            result.append(neg[index])
    if len(pos) < len(neg):
        for i in neg[len(pos):]:
            result.append(i)
    return result


sort_method([1, 2, 3, 7, 9, -5, -3, -4, -7, -8, -11, -3, -2])