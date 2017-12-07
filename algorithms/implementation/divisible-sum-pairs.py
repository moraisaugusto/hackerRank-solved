#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function

    total = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                total += 1

    return total



n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
