#!/bin/python3

import math
import os
import random
import re
import sys



def calc(s):
    a = 0
    vowel = "aeiou"
    for i in vowel:
        a += s.count(i)
    return a

def findSubstring(s, k):
    ans = "Not found!"
    count = 0
    for i in range(len(s)-k+1):
        temp = s[i:i+k]
        c = calc(temp)
        print(temp,c)
        if(c > count):
            count = c
            ans = temp
    return ans

s = "rishi"
k = 3
print(findSubstring(s,k))