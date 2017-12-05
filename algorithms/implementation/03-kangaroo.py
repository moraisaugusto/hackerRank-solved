#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function

    k1 = x1
    k2 = x2

    if k1 == k2:
        return "YES"

    if k1 != k2 and v1 == v2:
        return "NO"

    if (k1 < k2 and v1 < v2) or (k2 < k1 and v2 < v1):
        return "NO"

    prevDist = k2 - k1

    if prevDist > 0:
        flag = True
    else:
        flag = False

    while True:
        k1 = k1 + v1
        k2 = k2 + v2
        diff = k2 - k1

        if prevDist < 0 and flag == True:
            return "NO"

        if prevDist < diff + 1:
            return "NO"

        if k1 == k2:
            return "YES"

        prevDist = diff


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
