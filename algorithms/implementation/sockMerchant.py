#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

def sockMerchant(n, ar):
    # Complete this function

    sockPair = {}

    for i in ar:
        if i in sockPair:
            total = sockPair[i]
            sockPair[i] = total + 1
        else:
            sockPair[i] = 1


    total = 0
    for i in sockPair:
        total += int(sockPair[i]/2)

    return total


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
