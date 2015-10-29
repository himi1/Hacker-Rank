__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/staircase'''


import sys
n = int(raw_input())
i = 0
while i < n:
    print " " * (n - i - 1) + "#" * (i+1)
    i += 1