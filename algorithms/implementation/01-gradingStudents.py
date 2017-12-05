#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def solve(grades):
    # Complete this function
    finalGrades = []

    for i in grades:
        if i < 38:
            finalGrades.append(i)
        else:
            if i % 5 > 2:
                x = 5 - (i % 5)
                finalGrades.append(i + x)
            else:
                finalGrades.append(i)

    return finalGrades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
