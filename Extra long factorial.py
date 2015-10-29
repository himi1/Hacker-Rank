__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/extra-long-factorials'''


n = int(raw_input())
i = 2
output = 1
while i <= n:
    output = output * i
    i = i + 1
print output