#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input().strip())
p = 5

like = int(p/2)
dislike = p - like

share = like + dislike
totalLike = like
for i in range(1, n):
    share = like*3
    like = int(share/2)
    totalLike += like

print(totalLike)
