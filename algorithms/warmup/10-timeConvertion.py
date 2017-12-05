#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def timeConversion(s):
    # Complete this function
    hourType = s[-2:]
    hh, mm, ss = s[:-2].split(':')

    if hourType == "AM" and int(hh) <= 11 and int(mm) <= 59 and int(ss) <= 59:
        return ":".join([hh, mm, ss])

    if hourType == "PM" and int(hh) <= 11 and int(mm) <= 59 and int(ss) <= 59:
        hh = int(hh) + 12
        return ":".join([str(hh), mm, ss])

    if hourType == "AM" and int(hh) == 12:
        return ":".join(["00", mm, ss])

    if hourType == "PM" and int(hh) == 12:
        return ":".join(["12", mm, ss])

s = input().strip()
result = timeConversion(s)
print(result)

