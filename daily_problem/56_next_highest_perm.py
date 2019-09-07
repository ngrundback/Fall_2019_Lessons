# find the next highest perm of a num
# 123 => 132
# https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
def next_highest(arr):
    # start from the right most int 
    # and find first digit that is smaller than the int 
    # next to it
    n = len(arr)
    
    # move right
    for int in range(n-1,0,-1):
        if arr[int] > arr[int-1]:
            break 
    # if num not found, next digit is not possiable
    if int == 0:
        return 'Next number not possiable'
    
    # we want the number that breaks the pattern
    x = arr[int-1]
    # this is where we start the change
    smallest = int
    
    # find smallest digit on the right side of (int-1)
    for j in range(int+1, n):
        if arr[j] > x and arr[j] < arr[smallest]:
            smallest = j
    
    # swap the above found smallest with (int-1)
    arr[smallest], arr[int-1] = arr[int-1], arr[smallest]
    

    first_half = (arr[:int])
    second_half = sorted(arr[int:])
    
        
    return first_half + second_half
    
    
if __name__ == '__main__':
    arr = [1,2,3,4,2,1]
    print(next_highest(arr))