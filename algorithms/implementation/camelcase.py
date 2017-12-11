#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

s = input().strip()

total = 1
for i in s:
    if i.isupper():
        total += 1

print(total)
