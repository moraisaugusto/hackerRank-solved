#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    sum = 0
    for i in ar:
        sum = sum + i

    return sum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)

