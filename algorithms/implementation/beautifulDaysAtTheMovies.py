#!/usr/bin/env python
# -*- coding: utf-8 -*-

i,j,k = input().strip().split(' ')
i,j,k = [int(i),int(j),int(k)]

total = 0 
for x in range(i, j+1):
    reversed = int(str(x)[::-1])
    test = (x - reversed)/k
    if test.is_integer():
        total += 1
print(total)
