import random
import sys
from picture import Picture, Colour

class Maze(object):
    """docstring for Maze ."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [None] * (width * height)
        for i in range(width*height):
            self.grid[i] = Cell()

    def get_cell(self, x, y):
        return self.grid[y * self.width + x]

    def wall_to_east(self, x,y):
        cell = self.get_cell(x,y)
        cell2 = self.get_cell(x+1,y)
        wall = Wall(cell, cell2)
        cell.walls['east'] = wall
        cell2.walls['west'] = wall



    def wall_to_south(self, x,y):
        cell = self.get_cell(x,y)
        cell2 = self.get_cell(x,y+1)
        wall = Wall(cell,cell2)
        cell.walls['south'] = wall
        cell2.walls['north'] = wall

    def generate(self):
        for y in range(self.height-1):
            for x in range(self.width-1):
                self.wall_to_east(x,y)
                self.wall_to_south(x,y)

        for y in range(self.height-1):
            self.wall_to_south(self.width-1,y)

        for x in range(self.width-1):
            self.wall_to_east(x,self.height-1)

        start = self.get_cell(0,0)
        start.visited = True
        wall_list = []
        for wall in start.walls.values():
            if(wall is not None):
                wall_list.append(wall)

        while wall_list:

            index = random.randint(0,len(wall_list)-1)
            wall = wall_list.pop(index)
            cell1 = wall.cell1
            cell2 = wall.cell2
            if cell1.visited ^ cell2.visited: #if only one is visited/not visisted
                unvisited_cell = cell2 if cell1.visited else cell1
                wall.passage = True
                unvisited_cell.visited = True

                for adjacent_wall in unvisited_cell.walls.values():
                    if adjacent_wall and not adjacent_wall.passage:
                        wall_list.append(adjacent_wall)

    def to_picture(self):
        pic = Picture(self.width*4+1, self.height*4+1)
        for j in range(self.height):
            for i in range(self.width):

                for y in range(1+j*4,4+j*4):
                    for x in range(1+i*4,4+i*4):
                        pic.colour_pixel(x,y,Colour.WHITE)

                cell = self.get_cell(i,j)
                n = cell.walls['north']
                s = cell.walls['south']
                e = cell.walls['east']
                w = cell.walls['west']
                if(n and n.passage):
                    pic.colour_pixel(i*4+2,j*4+2-2,Colour.WHITE)
                if(s and s.passage):
                    pic.colour_pixel(i*4+2,j*4+2+2,Colour.WHITE)
                if(e and e.passage):
                    pic.colour_pixel(i*4+2+2,j*4+2,Colour.WHITE)
                if(w and w.passage):
                    pic.colour_pixel(i*4+2-2,j*4+2,Colour.WHITE)



        return pic

class Cell(object):
    """docstring for Cell."""

    id = 0

    def __init__(self, walls=None):
        self.visited = False
        self.walls = {
            'north' : None,
            'south' : None,
            'east'  : None,
            'west'  : None
        }
        self.id = Cell.id
        Cell.id += 1



class Wall(object):

    id = 0

    def __init__(self, cell1=None, cell2=None, passage=False):
        self.cell1 = cell1
        self.cell2 = cell2
        self.passage = passage
        self.id = Wall.id
        Wall.id+=1


def main():
    maze = Maze(int(sys.argv[1]),int(sys.argv[2]))
    maze.generate()
    maze.to_picture().to_PNG(sys.argv[3])

if __name__ == '__main__':
    main()
