#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

S = input().strip()

wordComplete = 0
sos = "SOS"*int(len(S)/3)

for i  in range(0, len(S), 1):
    if S[i] != sos[i]:
        wordComplete += 1

print(wordComplete)

