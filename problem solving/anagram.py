#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if(len(s)%2!=0):
        return -1
    else:
        s1=s[:(len(s)//2)]
        s2=s[(len(s)//2):]
        c=[0,0]
        for i in s1:
            if(i not in s2):
                c[0]+=1
        for j in s2:
            if(j not in s1):
                c[1]+=1        
        return max(c)

    
print(anagram("fdhlvosfpafhalll"))

    
