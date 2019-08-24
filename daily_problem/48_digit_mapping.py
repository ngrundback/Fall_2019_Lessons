def get_perms(digits, mapping):
    digit = digits[0]
    
    if len(digits) == 1:
        return mapping[digit]
    
    result = []
    
    for char in mapping[digit]:
        for perm in get_perms(digits[1:], mapping):
            print(perm)
            result.append(char + perm)
    return result
    


if __name__ == '__main__':
    mapping = {'1': ['a','b','c'], '2':['d','e','f'], '3':['h','i','j']}
    print(get_perms(['1','2','3'], mapping))