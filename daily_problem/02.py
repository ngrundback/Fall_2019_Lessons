# product of every number save for i
arr = [1,2,3,4,5]
def product(arr):
    count = 0
    length = len(arr)
    ans = []
    while count < length:
        num = 1
        exclude_num = arr[count]
        for x in arr:
            if x != exclude_num:
                num = num * x
        count += 1
        ans.append(num)
    return ans
print(product(arr))
