# given an array arr and num k, return true if any two numbers in arr add up to a given number k.

# O(n2)
def nested(arr, num):
    ans = []
    length = len(arr)
    for x in range(length-1):
        for y in range(x+1,length):
            if arr[x]+arr[y] == num:
                ans.append((arr[x],arr[y]))
    return ans

# O(n)
def count_down(arr,num):
    for x in range(num):
        y = num - x
        if x in arr and y in arr:
            return True
    return False


def linear_time(arr,num):
    for x in arr:
        num2 = num - x
        if num2 in arr:
            return True
    return False


#O(n/2)
def half_time(arr, num):
    new_list = range(len(arr)//2+1)
    for x in new_list:
        num2 = num - x
        if num2 in arr:
            return True
    else:
        return False

my_nums = [10,15,3,7]
print(nested(my_nums, 17))
print(count_down(my_nums, 17))
print(linear_time(my_nums, 17))
print(half_time(my_nums, 17))
