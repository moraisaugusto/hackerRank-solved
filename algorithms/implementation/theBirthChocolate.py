#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def solve(n, s, d, m):
    # Complete this function

    total = 0
    for i in range(0, len(s)):
        square = 0
        if i + m > len(s):
            k = len(s)
        else:
            k = i + m
        for j in range(i, k):
            square += s[j]

        if square == (d):
            total += 1
        square = 0

    return total


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
