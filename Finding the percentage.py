__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/finding-the-percentage'''

n = int(raw_input())
marks = {}
for i in range(0,n):
    input = raw_input().split()
    marks[input[0]] = float(input[1]) + float(input[2]) + float(input[3])

name = raw_input()
print "%.2f" % float(marks[name]/3)
