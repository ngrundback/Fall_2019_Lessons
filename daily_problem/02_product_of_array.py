# product of every number save for i
#from functools import reduce
import numpy

arr = [1,2,3,4,5]
#arr = [3,2,1]
# O(n2)
def product(arr):
    count = 0
    length = len(arr)
    ans = []
    while count < length:
        num = 1
        exclude_num = arr[count]
        for x in arr:
            if x != exclude_num:
                num = num * x
        count += 1
        ans.append(num)
    return ans
print(product(arr))

def division(arr):
    #product = reduce((lambda x, y: x* y), arr)
    product = numpy.prod(arr)
    ans = []
    for x in arr:
        num = product//x
        ans.append(num)
    return ans

print(division(arr))
