__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/pangrams'''


import string

input = raw_input()
input = set(input.lower())
#print input
if len(input) >= 26 and list(input)[len(input) - 26] == "a":
    print "pangram"
else:
    print "not pangram"

'''def ispangram(sentence, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(sentence.lower())

print ( ispangram(input('Sentence: ')) )'''