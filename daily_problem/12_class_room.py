def how_many_rooms(classes):
    # sort by start time
    #classes.sort(key = lambda x: x[0])
    n = len(classes)
    rooms = [0]*n
    rooms[0] = classes[0][1]

    for x in range(1,n):
        for y in range(x):
            if classes[x][0] > rooms[y]:
                rooms[y] = classes[x][1]
                break
    return n - rooms.count(0)



classes = [(30,75),(0,50), (60,150)]
print(how_many_rooms(classes))
