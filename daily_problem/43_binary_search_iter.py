def b_search(arr, target):
    low = 0
    high = len(arr) -1
    while True:
        mid = low + (high - low)//2
        if low > high:
            return None
        elif arr[mid] == target:
            return True
        elif arr[mid] < high:
            high = mid - 1
        else:
            low = mid + 1

            
    