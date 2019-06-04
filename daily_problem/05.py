# given the mapping a=1,b=2, etc
# count the number of ways a message can be decoded
# ex. 111 = 3
# 'aaa', 'ak', 'ka'
# 011 would not be permitted as no letter starts with 0

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
print(num_encoding('121212'))
#
# def nums(s):
#     # single baby
#     if len(s) == 1:
#         return 1
#     # endcase
#     if s[0] == '0':
#         return 0
#     # init data structures
#     cache = {}
#     # reverse loop. So, set last value to 1 as end conditions have been met.
#     cache[len(s)] = 1
#     # from the idx -1 to idx 0
#     for num in reversed(range(len(s))):
#         # no number starts with 0
#         if s[num] == '0':
#             cache[num] = 0
#         # ensures our else statement can work
#         # just count it as a single num
#         elif num == len(s) - 1:
#             cache[num] = 1
#         # if two elements are less than or == 26
#         else:
#             # parse from num to one ahead
#             if int(s[num:num + 2]) <= 26:
#                 # num is == to grand_father_value(two ahead)
#                 cache[num] = cache[num + 2]
#             # num is == to father value (one ahead)
#             cache[num] += cache[num+1]
#     return cache[0]
# print(nums('111'))

def count_me(s):
    s = [int(x) for x in s]

    # end cases
    if len(s) == 1:
        return 1
    if s[0] == 0 or s[0] > 2:
        return 0

    # data structures
    cache = {}
    cache[0] = 1

    for x in range(1,len(s)):

        if s[x] == 0:
            cache[x] == 0

        elif x <= 1:
            cache[x] = cache[0] + 1

        else:
            add_num = int( str(s[x-1]) + str(s[x-2]) )
            cache[x] = cache[x-1]
            if add_num <= 26:
                cache[x] += cache[x-2]



    return cache[len(s)-1]
print(count_me('121212'))
