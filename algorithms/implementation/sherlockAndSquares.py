#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
n = int(input().strip())

for i in range(n):
    a, b = input().split(' ')
    a, b = int(a), int(b)

    # I need to confess. I didn't know this formula
    print(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

