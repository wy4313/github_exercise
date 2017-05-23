#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def outputest():
    """ this function is write to test python
    1 print \' == '
    2 print \\ == \
    """
    print("I\'m \"ok\"")
    print('I\'m learning\nPython.')
    print('\\')
    print(r'[\\\t\\] output is [%s]' % '\\\t\\')

    str1 = 'ABC'
    str2 = str1
    str1 = 'abc'
    print('str1 is', str1, 'str2 is', str2)

    print('9/3=', 9 / 3, '9//3=', 9 // 3, '9//2=', 9 // 2, '9%2=', 9 % 2)

    print(outputest.__doc__)


if __name__ == '__main__':
    outputest()
