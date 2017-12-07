#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here

heighest = height[0] 
for i in height:
    if i > heighest:
        heighest = i

beverages = heighest - k

if beverages <= 0:
    print(0)
else:
    print(beverages)
