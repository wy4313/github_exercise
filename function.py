#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def my_abs(num):
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')
    if num < 0:
        return -num
    else:
        return num


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


if __name__ == '__main__':
    print(my_abs(-1))
    print(my_abs(10))
    print(my_abs(-0.0))
    print(my_abs(0))

    print(move(1,2, 4))
