#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

if n != len(arr):
    print ('Size of Array doesn`t match')
else:
    sum = 0
    for i in arr:
        sum = sum + i
    print(sum)

