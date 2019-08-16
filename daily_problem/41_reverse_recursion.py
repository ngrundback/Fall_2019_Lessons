def reverse(arr):
    if len(arr) == 0:
        return []
    print(arr[-1])
    return [arr[-1]] + reverse(arr[:-1])

print(reverse([1,2,3,4,5]))