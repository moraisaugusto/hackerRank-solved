#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

p_sum = 0
s_sum = 0
for i in range(n):
    p_sum = p_sum + a[i][i]
    s_sum = s_sum + a[i][n-i-1]

print(abs(p_sum - s_sum))

