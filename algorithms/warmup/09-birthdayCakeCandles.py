#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    tallest = ar[0]
    countTallest = 0

    for i in ar:
        if i > tallest:
            tallest = i
            countTallest = 0
        if i == tallest:
            countTallest = countTallest + 1

    return countTallest

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)

