#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

n = int(input().strip())

for i in range(1, n+1, 1):
    for j in range(n-i):
        print(" ", end="")
    print("#"*i)

