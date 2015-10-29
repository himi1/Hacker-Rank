__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/diagonal-difference'''


n = int(raw_input())
a = 0
b = 0
i = 0
while i < n:
    input = raw_input().split()
    a = a + int(input[i])
    b = b + int(input[n - i - 1])
    i = i + 1

output = max(a,b) - min(a,b)
print output