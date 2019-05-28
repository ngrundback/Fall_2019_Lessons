# given an array, return true if any two numbers add up to a give number
# O(n2)
def any_two(arr, num):
    ans = []
    length = len(arr)
    for x in range(length-1):
        for y in range(x+1,length):
            if arr[x]+arr[y] == num:
                ans.append((arr[x],arr[y]))
    return ans
my_nums = [10,15,3,7]
print(any_two(my_nums, 17))

# O(n)
def same_num(arr,num):
    for x in range(num):
        y = num - x
        if x in arr and y in arr:
            return True
    return False

my_nums = [10,15,3,7]
print(same_num(my_nums, 17))
