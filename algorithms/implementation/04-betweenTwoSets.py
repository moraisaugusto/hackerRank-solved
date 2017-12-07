#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def getTotalX(a, b):
    # Complete this function
    x = []
    
    highest = 0
    for i in a:
        if i > highest:
            highest = i


    lowest = 100 
    for i in b:
        if i < lowest:
            lowest = i
        

    for i in range(lowest, highest):



    total = 0

    return total


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
