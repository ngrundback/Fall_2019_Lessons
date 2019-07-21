def cut_cake(cake, num):
    # turn into 2D array
    pie =  list(map(list, cake.splitlines()))
    rl = len(pie)
    cl = len(pie[0])
    rasin_cords = []
    # check rows
    for x in range(rl):
        for y in range(cl):
            if 'o' == pie[x][y]:
                rasin_cords.append((x,y))



    return rasin_cords

    # find how many rasins
    # backtracking
        # is safe conditions
        # loop :)

cake = '''
........
..o.....
...o....
........
'''.strip()

print(cut_cake(cake,2))
