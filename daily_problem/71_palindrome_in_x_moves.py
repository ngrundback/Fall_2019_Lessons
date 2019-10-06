def x_pal(s, m):
    # base case
    if len(s) <= 1:
        return True
    # remove matching ends
    while s[0] == s[-1]:
        s = s[1:-1]
        if len(s) <= 1:
            return True
    if m == 0:
        return False
    
    # try ridding first & last characters
    return x_pal(s[:-1], m-1) or x_pal(s[1:], m-1)
    
print(x_pal('tacoscat',1))
x = 'tacocat'
print(x[::-1])