#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def getRecord(s):
    # Complete this function

    countHeighest = 0 
    countLowest = 0 
    heighest = s[0]
    lowest = s[0]
    for i in range(1, len(s)):
        if s[i] > heighest:
            countHeighest += 1
            heighest = s[i]
        if s[i] < lowest:
            countLowest += 1
            lowest = s[i]

    return [countHeighest, countLowest]


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
