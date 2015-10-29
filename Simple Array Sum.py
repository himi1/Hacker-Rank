__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/simple-array-sum'''


n = int(raw_input())
a = raw_input().split()
i = 0
output = 0
while i < n:
    output = output + int(a[i])
    i += 1
print output
