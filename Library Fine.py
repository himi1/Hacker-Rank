__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/library-fine'''


actual = raw_input().split()
exp = raw_input().split()
if int(exp[2]) < int(actual[2]):
    print 10000
elif int(exp[2]) == int(actual[2]):
    if int(exp[1]) < int(actual[1]):
        print ((int(actual[1]) - int(exp[1])) * 500)
    elif int(exp[1]) == int(actual[1]):
        if int(exp[0]) < int(actual[0]):
            print ((int(actual[0]) - int(exp[0])) * 15)
        else:
            print 0

