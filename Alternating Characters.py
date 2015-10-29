__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/alternating-characters'''


t = raw_input()
i = 0
while i < t:
    count = 0
    s = list(raw_input())
    j = 0
    while j < len(s) - 1:
        if s[j] == s[j+1]:
            count += 1
        j += 1
    print count
    i += 1