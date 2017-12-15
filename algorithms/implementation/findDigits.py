#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    m = list(map(int, str(n)))

    mSize = 0
    for i in m:
        if i != 0:
            if n % i == 0:
                mSize += 1

    print(mSize)

