# This problem was asked by Google.
# 
# Given two strings A and B, return whether or not A can be 
# shifted some number of times to get B.
# 
# For example, if A is abcde and B is cdeab, return true. 
# If A is abc and B is acb, return false.


def shifted(a,b):
    a,b = list(a), list(b)
    n,m = len(b), len(a)
    if n != m:
        return False
    count = 0
    while n > count:
        if a == b:
            return True, count
        temp = b.pop(-1)
        b.insert(0,temp)
        count += 1
    return False
    
a = "abcde"
b = "cdeab"
a2 = 'abc'
b2 = 'acb'
print(shifted(a,b))