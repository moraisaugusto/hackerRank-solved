#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos = 0
neg = 0
zer = 0

for i in arr:
    if i > 0:
        pos = pos + 1
    elif i < 0:
        neg = neg + 1
    else:
        zer = zer + 1

print (pos/n)
print (neg/n)
print (zer/n)

