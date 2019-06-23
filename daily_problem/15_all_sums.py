def exp_sum(n):
    # make table
    cache = [0] * n
    # idx of last num
    i = 0
    # first num is itself
    cache[i] = n

    while True:
        # find the right most non 1 value
        rm = 0
        while i >= 0 and cache[i] == 1:
            rm += cache[i]
            i -= 1

        if i < 0:
            return len(cache)

        cache[i] -= 1
        rm += 1



        while rm > cache[i]:
            cache[i+1] = cache[i]
            rm = rm - cache[i]
            i += 1

        cache[i + 1] = rm
        i+= 1

#print(exp_sum(4))

# all combos

def all_combos(n, arr):
    length = len(arr)
    cache = [0] * (n+1)
    cache[0] = 1

    for x in range(1, length+1):
        for y in range(length):
            if x >= arr[y]:
                cache[x] += cache[x - arr[y]]
    return cache[n]


print(all_combos(3, [1,2,3]))
