__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/plus-minus'''


n = int(raw_input())
i = 0
a = raw_input().split()
positive_count = float(0)
negative_count = float(0)
zero_count = float(0)
while i < n:
    if int(a[i]) < 0:
        negative_count += 1
    elif int(a[i]) > 0:
        positive_count += 1
    else: # int(a[i]) == 0:
        zero_count += 1
    i += 1
print "%.6f" % (positive_count/n)
print "%.6f" % (negative_count/n)
print "%.6f" % (zero_count/n)