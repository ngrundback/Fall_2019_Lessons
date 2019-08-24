def para_me(n):
    o = 0
    c = 0
    for x in n:
        if x == '(':
            o+=1
        elif x == ')':
            c+=1
    if c > o:
        return c - o
    return o - c
