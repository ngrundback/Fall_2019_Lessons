
def find_missing(arr):
    # could use merge sort
    arr.sort()
    length = range(len(arr)-1)
    for x in length:
        if arr[x] >= 0:
            if arr[x] - arr[x+1] < -1:
                return arr[x] + 1
    return arr[-1]+1

def find_missing2(arr):
    length = len(arr)
    arr.sort()
    if 1 not in arr:
        return 1
    one = arr.index(1)
    for x in range(one,length-1):
        if arr[x] - arr[x+1] < -1:
            return arr[x] + 1
    return arr[-1] + 1

def merge_sort(arr):
    pass

# 0(n2)
def bubble_sort(arr):
    length = len(arr)
    for x in range(length):
        swap = False
        for y in range(0,length-x-1):
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]
                swap = True
        if swap == False:
            return arr
    return arr




# Test Cases

# arr = [3,4,-1,1]   #= 2
# arr = [1,2,0]      #= 3
# arr = [0,2,-1]     #= 1


#print(find_missing(arr))
#print(bubble_sort(arr))
print(find_missing2(arr))
