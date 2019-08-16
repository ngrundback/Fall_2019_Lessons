def order_by_one(arr):
    n = len(arr)
    change = 0
    for n in range(n-1):
        if arr[n] > arr[n+1]:
            change += 1
    
    if change > 1:
        return False
    return True
    
print(order_by_one([10,5,7]))