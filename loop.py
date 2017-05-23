#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def HelloMsg():
    classmates = ['hello', 'world', 'python']
    for x in classmates:
        print('Hello %s' % x)


def calcsum(max):
    sumnumber = 0
    for i in range(max):
        sumnumber += i
    print(sumnumber)


if __name__ == '__main__':
    HelloMsg()
    while 'y' != input('do u want to exit?(y/n):'):
        maxnumber = input('input a sum max number(int):')
        calcsum(int(maxnumber))
