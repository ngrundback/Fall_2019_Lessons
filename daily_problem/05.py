def num_encoding(s):
    # one letter = 1 combo
    if len(s) <= 1:
        return 1
    # empty string is None
    if s[0] == '0':
        return 0
    total = 0
    # recurisvely call
    if int(s[:2]) <= 26:
        total += num_encoding(s[2:])

    total += num_encoding(s[1:])
    return total


def nums(s):
    # single baby
    if len(s) == 1:
        return 1
    # endcase
    if s[0] == '0':
        return 0
    # init data structures
    cache = {}
    # reverse loop. So, set last value to 1 as end conditions have been met.
    cache[len(s)] = 1
    # from the idx -1 to idx 0
    for num in reversed(range(len(s))):
        print(s[1:3])
        # no number starts with 0
        if s[num] == '0':
            cache[num] = 0
        # ensures our else statement can work
        # just count it as a single num
        elif num == len(s) - 1:
            cache[num] = 1
        # if two elements are less than or == 26
        else:
            # parse from num to one ahead
            if int(s[num:num + 2]) <= 26:
                # num is == to past value
                cache[num] = cache[num + 2]
            # num is == to past value
            cache[num] += cache[num+1]
    return cache[0]
print(nums('123'))

num = '1234'
x = 1
print(num[x:x+2])
print(num[x+2])
print(num[x+1])
