#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def testif():
    height = float(input("input your height(m):"))
    print("your height is:", height)
    weight = float(input("input your weight(kg):"))
    print("your weight is:", weight)

    bmi = weight / height
    print("%f/%f=%f(bmi)" % (weight, height, weight / height))
    if(bmi < 18.5):
        print("过轻")
    elif(bmi < 25):
        print("正常")
    elif(bmi < 28):
        print("过重")
    elif(bmi < 32):
        print("超重")
    else:
        print("严重肥胖")


if __name__ == "__main__":
    while 'y' != input('do you want to exit?(y/n):'):
        testif()
