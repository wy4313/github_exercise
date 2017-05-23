#!/usr/bin/env python3
# -*-coding: utf-8 -*-


def strencoding():
    a = ord('A')
    print(a)
    b = ord('中')
    print(b)

    x = b'ABC'
    print(x)
    for i in x:
        print('%04d %0.2f 0x%X'%(i, i, i), end=' ')
    print()

    str1 = '中国'.encode(encoding='utf_8')
    print(str(str1), 'encode with utf-8 is', str1)

    print('len(\'中国\') is:', len('中国'));
    print('len(\'ABC\') is:', len('ABC'));
    print('len(b\'abc\') is:', len(b'abc'))
    print('len(\'中国\'.encode(utf-8) is:', len(str1))


if __name__ == '__main__':
    strencoding()
