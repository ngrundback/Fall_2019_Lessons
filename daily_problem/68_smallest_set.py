# This problem was asked by Google.
# 
# Given a set of closed intervals, find the smallest set of numbers 
# that covers all the intervals. If there are multiple smallest sets, return any of them.
# 
# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of 
# numbers that covers all these intervals is {3, 6}.

def smallest_set(arr):
    # sort by last value
    # must sort to work
    arr.sort(key=lambda x: x[1])
    print(arr)
    ans = []
    last = None
    
    # cycle through sets
    for interval in arr:
        # find the smallest 
        # No worries about duplicate ints
        if last == None or last < interval[0]:
            # update smallest
            last = interval[1]
            # update ans
            ans.append(last)
    return ans
        
if __name__ == '__main__':
    arr = [[0, 3], [12, 6], [3, 4], [6, 9]]
    print(smallest_set(arr))
