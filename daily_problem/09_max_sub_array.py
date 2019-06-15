# O(n*k)
def max_sub(arr,k):
    for x in range(len(arr)-k+1):
        print(max(arr[x:x+k]))

arr = [10,5,2,7,8,7]
print(max_sub(arr,3))
