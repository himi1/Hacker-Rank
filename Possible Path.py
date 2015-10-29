__author__ = 'Himanshi'

'''Question URL: https://www.hackerrank.com/challenges/possible-path'''


def gcd(u, v):
    if u==v:
        return u
    if u==0:
        return v
    if v==0:
        return u
    if ~u & 1:
        if v&1:
            return gcd(u>>1, v)
        else:
            return gcd(u>>1, v>>1)<<1
    if ~v & 1:
        return gcd(u, v>>1)
    if u>v:
        return gcd((u-v)>>1, v)
    return gcd((v-u)>>1, u)


t = int(raw_input())
while t > 0:
    a, b, x, y = raw_input().split()
    m=gcd(int(a), int(b))
    n=gcd(int(x), int(y))
    if m==n:
        print "YES"
    else:
        print "NO"
    t = t - 1