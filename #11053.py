#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:21:53 2022

@author: jun
"""

A = int(input())
Ai = list(map(int, input().split()))

cnt = [1 for x in range(A)]


for i in range(A):
    for j in range(i):
        if Ai[i] > Ai[j]:
            cnt[i] = max(cnt[i],cnt[j]+1)
            
print(max(cnt))