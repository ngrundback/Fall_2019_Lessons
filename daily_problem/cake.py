def cut_cake(cake):
    # turn into 2D array
    pie =  list(map(list, cake.splitlines()))
    # row_l = (len(pie)//2)
    # col_l = (len(pie[0])//2)
    # top_half = pie[:row_l][:col_l]
    #print(top_half)
    top_left = pie[:2]
    print(top_left)

cake = '''
........
..o.....
...o....
........
'''.strip()

print(cut_cake(cake))
