from math import comb as nCr
a, b = input(), input()
n = b.count('?')
r = a.count('+') - b.count('+')
print(0.0 if n<r or r<0 else nCr(n, r)/(2**n))