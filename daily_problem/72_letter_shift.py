# This problem was asked by Facebook.
# 
# Write a function that rotates a list by k elements. For example, 
# [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. Try 
# solving this without creating a copy of the list. How many swap or 
# move operations do you need?


# circle movement
def rotate(lst, m):
    count = len(lst)-m
    for x in range(m):
        swap(x,count,lst)
        count += 1
    return lst
    
def swap(front, back, lst):
    temp = lst[back]
    lst[back] = lst[front]
    lst[front] = temp
    return lst

# rotate lst    
def crotate(lst, m):
    # for each move
    for _ in range(m):
        # first element is stored
        first_element = lst[0]
        # moves on down one
        # last item will be recorded twice
        for i in range(len(lst)-1):
            lst[i] = lst[i+1]
            #print(lst)
        # So, the last element is switched to first element
        lst[-1] = first_element
    return lst

arr = [1, 2, 3, 4, 5, 6]
print(crotate(arr,2))