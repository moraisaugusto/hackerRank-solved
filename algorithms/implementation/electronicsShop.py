#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    total = keyboards[0] + drives[0] 

    if total > s:
        total = -1

    for i in keyboards:
        for j in drives:
            if i + j <= s and i + j > total:
                total = i + j

    return total


s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
