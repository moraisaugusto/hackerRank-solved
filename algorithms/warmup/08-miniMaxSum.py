#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

values = [a, b, c, d, e]

min = values[0]
max = values[0] 
for i in values:
    if i < min:
        min = i
    elif i > max:
        max = i

print(sum(values)-max, sum(values)-min)

