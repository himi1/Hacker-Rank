__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/contests/yhxh9bxejzv/challenges/cs5800hw1modularexponentation'''


# Modular Exponentation
# Given:    positive integers a and n, and a non-negative integer x
# Result:   a^x mod n

input = raw_input()                     # input = "a x n"
input_list = input.split(' ')           # input_list = ["a", "x", "n"]
a = int(input_list[0])                  # a -> base
x = int(input_list[1])                  # x -> exponential power
n = int(input_list[2])                  # n -> modulus


def mod_expo(a, x, n):
    result = 1
    a = a % n                           # a in (mod n)
    while x > 0:                        # while x is greater than 0
        print a                         # prints the values of a^1, a^2, a^4 and so on...
        if (x & 1 == 1):                # if right most bit of x is 1, i.e x is odd then:
            result = (result * a) % n   # multiply number by a in (mod n)
        x = x >> 1                      # bit shifting to right by one place
        a = (a * a) % n                 # a getting sqaured in (mod n)
    return result

print bin(x)[2:]                        # printing binary value of x
result = mod_expo(a, x, n)
print result                            # printing final result


