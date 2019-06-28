# what could go wrong

def balance(str):
    #score = 0
    cache = {}
    cache['('] = 0
    cache['{'] = 0
    cache['['] = 0
    for x in str:
        if x in cache:
            #score += 1
            cache[x] += 1
        else:
            if x == ')':
                cache['('] -= 1
            elif x == ']':
                cache['['] -= 1
            else:
                cache['{'] -= 1
            #score -= 1
            #cache[x] -= 1
    if 1 or -1 in cache.values():
        return False
    else:
        return True


print(balance('([])[][({})}'))
