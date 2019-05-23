from typing import NamedTuple, List, Dict, Optional
import random, pprint
Grid = List[List[str]]

class GridLocation():
    def __init__(self, rows,cols):
        self.rows = rows
        self.cols = cols
        self. grid = None

    def generate_grid(self):
        self.grid = [[random.randint(0,1) for c in range(self.cols)]for r in range(self.rows)]

    def display_grid(self):
        pprint.pprint(self.grid)

state1 = GridLocation(5,5)
state1.generate_grid()
state1.display_grid()
