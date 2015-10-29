__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/time-conversion'''


t = raw_input().split(":")
#print t
#print t[2][2:4]
if t[2][2:] == "PM":
    if t[0] == "12":
        print t[0] + ":" + t[1] + ":" + t[2][:2]
    else:
        print str((int(t[0]) + 12)) + ":" + t[1] + ":" + t[2][:2]
else:
    if t[0] == "12":
        print "00" + ":" + t[1] + ":" + t[2][:2]
    else:
        print t[0] + ":" + t[1] + ":" + t[2][:2]