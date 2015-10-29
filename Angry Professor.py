__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/angry-professor'''


t = int(raw_input())
i = 0
while i < t:
    input = raw_input().split()
    n = int(input[0])
    k = int(input[1])
    #print n, k
    a = raw_input().split()
    j = 0
    while j < n:
        if int(a[j]) <= 0:
            k = k - 1
        j += 1
    if k > 0:
        print "YES"
    else:
        print "NO"
    i += 1