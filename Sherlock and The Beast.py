__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/sherlock-and-the-beast'''


t = int(raw_input())
i = 0
while i < t:
    n = int(raw_input())
    c = 5*(2*n%3)
    if c > n:
        print(-1)
    else:
        print('5' * (n-c) + '3'*c)
    i += 1