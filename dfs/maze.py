import random, pprint
class Cell():
    def __init__(self,x,y, lvl):
        self.x = x
        self.y = y
        self.cost = random.randint(0,10)
        self.searched = False
        self.parent = None
        if self.cost < lvl and (self.x > 0 and self.y > 0):
            self.wall = True
        else:
            self.wall = False

def make_maze(row,col,lvl):
    matrix = [[Cell(x,y,lvl) for x in range(10)]for y in range(10)]
    return matrix

maze = make_maze(10,10,2)
#pprint.pprint(maze)
#print(maze[0][0].cost)
