#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    catA = z - x
    catB = z - y

    if abs(catA) > abs(catB):
        print("Cat B")
    elif abs(catB) > abs(catA): 
        print("Cat A")
    else:
        print("Mouse C")

