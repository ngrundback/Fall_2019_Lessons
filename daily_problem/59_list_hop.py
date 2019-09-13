# This problem was asked by Pinterest.
# 
# Given an integer list where each number represents the number of hops you can make, 
# determine whether you can reach to the last index starting at index 0.
# 
# For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

# works if you have to take max steps
def hop(arr):
    hops = 0
    n = len(arr)-1
    count = 0
    while count < n:
        hops = arr[count]
        count += hops
        if hops == 0 and count < n:
            return False
    return True


def dp_hop(arr):
    steps_left = 1
    
    for hop in range(len(arr)-1):
        steps_left = max(steps_left - 1, arr[hop])
        if steps_left == 0:
            return False
    return True
    
test1 = [1,1,0,1]
test2= [2,3,0,0,3,1,0]
print(hop(test2))
print(dp_hop(test2))