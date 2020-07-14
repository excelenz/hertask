def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    pass


# Python3 program to find a number that
# divides maximum array elements
import math as mt

MAXN = 100001

# stores smallest prime factor for
# every number
spf = [0 for i in range(MAXN)]


# Calculating SPF (Smallest Prime Factor)
# for every number till MAXN.
# Time Complexity : O(nloglogn)
def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        # marking smallest prime factor for
        # every number to be itself.
        spf[i] = i

        # separately marking spf for every
    # even number as 2
    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN + 1))):
        # checking if i is prime
        if (spf[i] == i):
            # marking SPF for all numbers divisible by i
            for j in range(2 * i, MAXN, i):
                # marking spf[j] if it is not
                # previously marked
                if (spf[j] == j):
                    spf[j] = i
                    # A O(log n) function returning primefactorization


# by dividing by smallest prime factor at every step
def getFactorization(x):
    ret = list()
    print("****************")
    while (x != 1):
        temp = spf[x]
        ret.append(temp)
        while (x % temp == 0):
            x = x // temp
            print("getFactorization {}".format(x))
    return ret

# Function to find a number that
# divides maximum array elements
def generalizedGCD(n, A):
    # precalculating Smallest Prime Factor
    sieve()
    # Hash to store frequency of each divisors
    m = dict()
    # Traverse the array and get spf of each element
    for i in range(n):
        # calling getFactorization function
        p = getFactorization(A[i])

        for i in range(len(p)):
            if p[i] in m.keys():
                m[p[i]] += 1
            else:
                m[p[i]] = 1

    cnt = 0
    ans = 10 ** 9 + 7

    for i in m:
        if (m[i] >= cnt):
            cnt = m[i]
            if ans > i:
                ans = i
            else:
                ans = ans

    return ans


# Driver Code
A = [33,15,45,27,21,66]
n = 5

print(generalizedGCD(n, A))




