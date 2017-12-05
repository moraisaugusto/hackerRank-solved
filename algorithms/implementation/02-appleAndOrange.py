#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

countApples = 0
for i in apple:
    if i > 0:
        print(i+a)
        print(s, t)
        if (i + a) in range(s,t+1):
            countApples = countApples + 1
    elif (i + a) in range(s, t):
        countApples = countApples + 1
countOranges = 0
for i in orange:
    if i < 0:
        if (i + b) in range(s, t+1):
            countOranges = countOranges + 1
    elif (i + b) in range(s, t):
        countOranges = countOranges + 1


print(countApples)
print(countOranges)

