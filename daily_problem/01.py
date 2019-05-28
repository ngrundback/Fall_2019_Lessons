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

print(same_num(my_nums, 17))

def linear_time(arr,num):
    for x in arr:
        num2 = num - x
        if num2 in arr:
            return True
    return False

print(linear_time(my_nums, 17))

#O(n/2)
def half_time(arr, num):
    for x in range(len(arr)//2+1):
        num2 = num - x
        if num2 in arr:
            return True
    else:
        return False
print(half_time(my_nums, 17))
