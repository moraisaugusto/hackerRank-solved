#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    annaCost = 0
    for i in range(len(ar)):
        if i != k:
            annaCost += ar[i]

    annaCost = annaCost / 2
    if float(b) > annaCost:
        return int(b - annaCost)
    else:
        return "Bon Appetit"


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
