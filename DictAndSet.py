#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def dictTest():
    score = {'hello': 98, 'world': 95, 'python': 85}
    print(score)

    score['hello'] = 97
    for key in score.keys():
        print(score[key])

    for key, value in score.items():
        print(key, ':', value)
        score[key] = value + 1
    print(score)

    value = score.pop('python')
    print(value)
    print(score)

    score['aaa'] = 12
    print(score)


def setTest():
    set1 = set(range(5))
    print(set1)

    set2 = set(range(1, 10, 2))
    print(set2)

    print(set2 - set1)
    print(set2 | set1)
    print(set2 & set1)


if __name__ == "__main__":
    dictTest()
    setTest()
