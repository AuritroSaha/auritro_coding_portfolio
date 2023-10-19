'''
With Big-O Notation, can ignore:
 - all terms except for the one with the highest degree (exponent)
 - any coefficients

 f(n) = 2n^1 + 4n^0 -> O(n)
'''

# f(n) = 12n^2 + n   O(n^2)


# f(n) = n - sqrt(n) + 0        O(n)


# f(n) = 11,000,000n + 5        O(n)


# f(n) = 1,000,000n - 1,000,000      O(n)


# f(n) = 1,234,567 + 6 - 5       O(1)


# f(n) = log(n) + 2      O(log(n))


# f(n) = n + log(n)      O(n)


# These next 3 are challenge problems!
# f(n) = 1 + 2 + 3 + 4 + 5 + 6 ... + (n-2) + (n-1) + n (The exact sum is n(n+1)/2)     O(n^2)

# (1 + n) + (2 + (n-1)) + (3 + (n - 2)) ... = (n + 1) * (n/2)


# f(n, m) = 3log2(n) + m^2       O(log(n) + m^2)

# f(n, m) =  3log2(n) * m^2      O(log(n)*m^2)


# f(n) = 1 + f(n//2) = log_2(n)     O(log(n))
# f(1) = 0

'''
n   f(n)
--------
1   0
2   1
3   1
4   2
5   2
6   2
7   2
8   3
16  4
32  5


2 ^ f(n) = n
f(n) = log_2(n)
'''


