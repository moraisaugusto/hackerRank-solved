#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()

highest = 0
for i in word:
    index  = ord(i)-97
    if h[index] > highest:
        highest = h[index]

print(len(word)*highest)
