def perms(arr):
    if len(arr) == 1:
        return [arr]
    
    output = []
    
    for x in perms(arr[1:]):
        for idx in range(len(arr)):
            output.append( x[:idx] + [arr[0]] + x[idx:] )
    return output


if __name__ == '__main__':
    print(perms([1,2,3]))