# Given string s and a bigger string b, find all permutations of s in b and print it's position
import numpy as np

def is_permutation(a, b):
    return np.array_equal(sorted(a), sorted(b))
    
s = "aab"
b = "ababbaaba"
for i in range(0, len(b) - len(s) + 1):
    # look at substrings of b of length len(s)
    # print b[i:(i+len(s))]
    if (is_permutation(b[i:(i+len(s))], s)):
        print i
        print b[i:(i+len(s))]  