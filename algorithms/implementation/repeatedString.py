#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

s = input().strip()
n = int(input().strip())

c = 0
for i in s:
    if i == "a":
        c += 1

if c == 0:
    print(0)
else:
    lbound = math.floor(n/len(s))
    j = 0
    total = lbound * c
    for i in range(lbound*len(s)+1, n+1):
        if s[j] == "a":
            total += 1

        j += 1
        if j >= len(s):
            j = 0

    print(total )

