#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

jumps = 0
i = 0
while(i < len(c)):
    if i+2 < len(c):
        if c[i+2] == 0:
            jumps += 1
            i += 2
        elif c[i+1] == 0:
            jumps += 1
            i += 1
    else:
        if c[len(c)-1] == 0:
            jumps += 1
            i += 1

print(jumps-1)

