__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/bigger-is-greater'''


t = int(raw_input())
i = 0
while i < t:
    found = 0
    w = list(raw_input())
    j = len(w) - 1
    while j >= 0 and found == 0:
        if w[j] > w[j-1]:
            found = 1
            temp = w[j]
            w[j] = w[j-1]
            w[j-1] = temp
        j -=1
    if found == 0:
        print "no answer"
    else:
        print "".join(w)
    i += 1