# This is your coding interview problem for today.
# 
# This problem was asked by Microsoft.
# 
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# 
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.
# 
# Your algorithm should run in O(n) complexity.
# 
# We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.
# 
# Have a great day!

def longest(arr):
    sorted_arr = merge_sort(arr)
    ans = []
    temp_ans = []
    up_to = 1
    start = 0
    for x in range(len(sorted_arr)-1):
        if sorted_arr[x] - 1 == sorted_arr[x+1]:
            print(sorted_arr[x]-1,  sorted_arr[x+1])
            up_to += 1
        else:
            temp_ans = sorted_arr[start:up_to]
            start = x+1
            up_to = x+2
            if len(temp_ans) > len(ans):
                ans = temp_ans
    
    temp_ans = sorted_arr[start:up_to]
         
    
    return ans, temp_ans
        
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        r = arr[mid:]
        l = arr[:mid]
        
        merge_sort(r)
        merge_sort(l)
        
        i,j,k = 0,0,0
    
        while i < len(r) and j < len(l):
            if r[i] > l[j]:
                arr[k] = r[i]
                i += 1
            else:
                arr[k] = l[j]
                j+=1
            k += 1
            
        while i < len(r):
            arr[k] = r[i]
            i+=1
            k+=1
        
        while j < len(l):
            arr[k] = l[j]
            j+=1
            k+=1
        #print(arr)
        return arr
            
    
if __name__ == '__main__':
    arr = [12,3,13,5,4,14,2,0]
    print(longest(arr))    
            
            