#!/usr/bin/python3

from time import sleep


def counter():
    a = 0
    print(a)
    sleep(1)
    while True:
        a += 1
        print(a)
        sleep(1)
    return
counter();